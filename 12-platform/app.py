"""Kilele TechPath platform prototype (Section 14 of the framework).

Features: coding playground, project submissions, technology passport,
teacher dashboard, specialization discovery and a moderated showcase.

This is a local prototype. See README.md before deploying it anywhere.
"""

from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path

from flask import (
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from pathways import PATHWAYS, recommend
from runner import run_python

BASE = Path(__file__).resolve().parent
DB_PATH = Path(os.environ.get("KILELE_DB_PATH", str(BASE / "data" / "kilele.db")))
TEACHER_PIN = os.environ.get("KILELE_TEACHER_PIN", "")

COMPETENCIES = [
    "Computer literacy", "Digital productivity", "Internet literacy",
    "Digital citizenship", "Computational thinking", "Programming",
    "Data literacy", "Hardware / electronics", "Networking",
    "AI awareness", "Creative technology", "Collaboration",
    "Project development",
]

SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    learner TEXT NOT NULL,
    grade TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    code TEXT,
    pathway TEXT,
    approved INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS competencies (
    learner TEXT NOT NULL,
    grade TEXT NOT NULL,
    competency TEXT NOT NULL,
    level INTEGER NOT NULL,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (learner, competency)
);
CREATE TABLE IF NOT EXISTS interests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    learner TEXT NOT NULL,
    scores TEXT NOT NULL,
    primary_pathway TEXT NOT NULL,
    complementary_pathway TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

app = Flask(__name__)
app.secret_key = os.environ.get("KILELE_SECRET_KEY", "dev-only-change-me")
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        g.db = connection
    return g.db


@app.teardown_appcontext
def close_db(_error=None) -> None:
    connection = g.pop("db", None)
    if connection is not None:
        connection.close()


def init_db() -> None:
    with app.app_context():
        get_db().executescript(SCHEMA)


init_db()


def teacher_ok() -> bool:
    return not TEACHER_PIN or session.get("teacher", False)


def require_teacher():
    if not teacher_ok():
        return redirect(url_for("login"))
    return None


@app.route("/")
def index():
    return render_template("index.html", pin_enabled=bool(TEACHER_PIN))


@app.route("/playground", methods=["GET", "POST"])
def playground():
    output = None
    preview = None
    code = request.form.get("code", 'print("Hello, Kilele TechPath!")')
    language = request.form.get("language", "python")

    if request.method == "POST":
        if language == "python":
            output = run_python(code)
        else:
            preview = code
            output = "Preview displayed in the sandbox frame below."

    return render_template(
        "playground.html", code=code, language=language,
        output=output, preview=preview,
    )


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        learner = request.form.get("learner", "").strip()
        title = request.form.get("title", "").strip()
        if not learner or not title:
            flash("Learner name and project title are required.")
            return redirect(url_for("submit"))

        get_db().execute(
            "INSERT INTO submissions (learner, grade, title, description, code, pathway) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                learner,
                request.form.get("grade", "").strip(),
                title,
                request.form.get("description", "").strip(),
                request.form.get("code", ""),
                request.form.get("pathway", "").strip(),
            ),
        )
        get_db().commit()
        flash(f"Project '{title}' submitted. A teacher can approve it for the showcase.")
        return redirect(url_for("submissions"))

    return render_template("submit.html", pathways=PATHWAYS)


@app.route("/submissions")
def submissions():
    rows = get_db().execute(
        "SELECT * FROM submissions ORDER BY created_at DESC, id DESC"
    ).fetchall()
    return render_template("submissions.html", rows=rows, can_approve=teacher_ok())


@app.route("/approve/<int:project_id>", methods=["POST"])
def approve(project_id: int):
    gate = require_teacher()
    if gate:
        return gate
    get_db().execute("UPDATE submissions SET approved = 1 WHERE id = ?", (project_id,))
    get_db().commit()
    flash("Project approved for the showcase.")
    return redirect(url_for("showcase"))


@app.route("/showcase")
def showcase():
    rows = get_db().execute(
        "SELECT * FROM submissions WHERE approved = 1 ORDER BY created_at DESC, id DESC"
    ).fetchall()
    return render_template("showcase.html", rows=rows)


@app.route("/passport", methods=["GET", "POST"])
def passport():
    learner = request.form.get("learner", "").strip() or request.args.get("learner", "").strip()

    if request.method == "POST":
        competency = request.form.get("competency", "")
        level = request.form.get("level", "")
        if not learner or competency not in COMPETENCIES or not level.isdigit():
            flash("Choose a learner, a competency and a level from 1 to 5.")
        elif not 1 <= int(level) <= 5:
            flash("Level must be between 1 and 5.")
        else:
            get_db().execute(
                "INSERT INTO competencies (learner, grade, competency, level) "
                "VALUES (?, ?, ?, ?) "
                "ON CONFLICT(learner, competency) DO UPDATE SET "
                "grade = excluded.grade, level = excluded.level, "
                "updated_at = CURRENT_TIMESTAMP",
                (learner, request.form.get("grade", "").strip(), competency, int(level)),
            )
            get_db().commit()
            flash("Competency record saved.")
        return redirect(url_for("passport", learner=learner))

    records = []
    if learner:
        records = get_db().execute(
            "SELECT competency, grade, level, updated_at FROM competencies "
            "WHERE learner = ? ORDER BY competency",
            (learner,),
        ).fetchall()

    return render_template(
        "passport.html", learner=learner, records=records, competencies=COMPETENCIES
    )


@app.route("/discover", methods=["GET", "POST"])
def discover():
    if request.method == "POST":
        learner = request.form.get("learner", "Anonymous").strip() or "Anonymous"
        scores: dict[str, int] = {}
        for number, pathway in enumerate(PATHWAYS):
            value = request.form.get(f"q{number}", "3")
            scores[pathway["name"]] = int(value) if value.isdigit() else 3

        first, second = recommend(scores)
        get_db().execute(
            "INSERT INTO interests (learner, scores, primary_pathway, complementary_pathway) "
            "VALUES (?, ?, ?, ?)",
            (learner, json.dumps(scores), first, second),
        )
        get_db().commit()

        return render_template(
            "discover.html", pathways=PATHWAYS, scores=scores,
            first=first, second=second, learner=learner, done=True,
        )

    return render_template("discover.html", pathways=PATHWAYS, done=False)


@app.route("/dashboard")
def dashboard():
    gate = require_teacher()
    if gate:
        return gate

    db = get_db()
    stats = {
        "submissions": db.execute("SELECT COUNT(*) FROM submissions").fetchone()[0],
        "approved": db.execute("SELECT COUNT(*) FROM submissions WHERE approved = 1").fetchone()[0],
        "competencies": db.execute("SELECT COUNT(*) FROM competencies").fetchone()[0],
        "learners": db.execute(
            "SELECT COUNT(DISTINCT learner) FROM competencies"
        ).fetchone()[0],
        "average_level": db.execute("SELECT AVG(level) FROM competencies").fetchone()[0],
    }
    recent = db.execute(
        "SELECT learner, grade, title, pathway, created_at FROM submissions "
        "ORDER BY id DESC LIMIT 8"
    ).fetchall()
    levels = db.execute(
        "SELECT learner, grade, ROUND(AVG(level), 2) AS average FROM competencies "
        "GROUP BY learner ORDER BY learner"
    ).fetchall()
    return render_template("dashboard.html", stats=stats, recent=recent, levels=levels)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if TEACHER_PIN and request.form.get("pin", "") == TEACHER_PIN:
            session["teacher"] = True
            flash("Teacher access enabled.")
            return redirect(url_for("dashboard"))
        flash("Incorrect PIN.")
    return render_template("login.html", pin_enabled=bool(TEACHER_PIN))


@app.route("/logout")
def logout():
    session.pop("teacher", None)
    flash("Teacher access ended.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("KILELE_HOST", "127.0.0.1"),
        port=int(os.environ.get("KILELE_PORT", "5000")),
        debug=False,
    )
