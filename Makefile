# Kilele TechPath — convenient shortcuts for repository checks and scaffolding.

.PHONY: check links docs fix examples setup setup-ai learner project

GRADE ?= grade-11
LEARNER ?= class
TEACHER ?= Not assigned

check:
	bash scripts/check-all.sh

links:
	bash scripts/validate-links.sh

docs:
	bash scripts/check-docs.sh

fix:
	bash scripts/check-docs.sh --fix

examples:
	bash scripts/run-examples.sh

setup:
	bash scripts/setup-environment.sh

setup-ai:
	bash scripts/setup-environment.sh --with-ai

# Usage: make learner NAME="Amina Otieno" GRADE=grade-8 TEACHER="Mr Kamau"
learner:
	bash scripts/new-learner.sh "$(NAME)" "$(GRADE)" "$(TEACHER)"

# Usage: make project TITLE="Grade Calculator" GRADE=grade-8 LEARNER=amina-otieno
project:
	bash scripts/new-project.sh "$(TITLE)" "$(GRADE)" "$(LEARNER)"
