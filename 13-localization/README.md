# Localization Framework

*Making Kilele TechPath usable in the languages of the learners it serves.*

English remains the source language. This folder provides a repeatable process for translated summaries and a shared termbase so that the same concept is translated consistently across grades, quizzes and the platform.

## Contents

| File | Purpose |
|---|---|
| [termbase.csv](termbase.csv) | Approved English → Kiswahili → French terms |
| [locales/sw/README.md](locales/sw/README.md) | Kiswahili programme summary |
| [locales/fr/README.md](locales/fr/README.md) | French programme summary |
| `scripts/localization.sh` | Validates the termbase and locale files |

## What is translated

Translations currently cover:

- Programme identity, vision, mission and guiding principles
- Grade stage names and competency names
- A short orientation for learners and teachers
- Key terminology through the termbase

The full curriculum, code examples and quizzes remain in English. Translate them incrementally, starting with the materials used in the classroom.

## How to add a language

1. Copy `locales/sw/README.md` to `locales/<code>/README.md`.
2. Translate the headings and content, keeping the links to English source documents.
3. Add a column to `termbase.csv` for the new language and fill every row.
4. Register the language code in `scripts/tools/check_localization.py`.
5. Run `bash scripts/localization.sh` and fix any reported issues.
6. Open a pull request with the translation and a note about the reviewer.

## Translation principles

- Keep meaning before word-for-word equivalence.
- Use the termbase for technical words so learners meet the same term every grade.
- Keep code, file names, commands and tool names in English — learners need those exact strings.
- Preserve safety language exactly: authorization, privacy and ethics must not be weakened in translation.
- Mark any section that is still untranslated rather than silently omitting it.

## Review workflow

1. Translator completes the locale file.
2. A second speaker reviews for accuracy and classroom appropriateness.
3. Automated check confirms links, term usage and required sections.
4. Maintainer merges and records the language in the release notes.

## Validation

```bash
bash scripts/localization.sh
```

The check reports missing files, empty translations, duplicate terms and locale files that do not use the approved terminology.

Related: [Full Curriculum](../TECH-PATH-CURRICULUM.md) · [Platform](../12-platform/README.md) · [Glossary](../08-resources/glossary.md)
