# Master To‑Do Checklist — AI Diploma 100% Practical Coverage

This is the **master checklist** for achieving and verifying **100% coverage** of practical activities based on `DETAILED_UNIT_DESCRIPTIONS.md`.

> Note: Some curriculum items are **discussion/presentation-based** (e.g., debates, policy writing, slide decks). Those are supported with guidance notebooks where appropriate, but they are not “code-only” requirements.

---

## Project Setup & Scaffolding

- [x] Confirm repository structure and course/unit folder conventions (`Course XX/unitY-*/examples`)
- [x] Ensure Git is initialized and baseline commit exists
- [x] Ensure `requirements.txt` exists and includes course-wide dependencies
- [x] Ensure core documentation exists (`README.md`, setup/handbook guides)

## Source-of-Truth Requirements Extraction

- [x] Use `DETAILED_UNIT_DESCRIPTIONS.md` as the official list of required practical activities
- [x] Maintain machine-readable tracking data (e.g., `ALIGNMENT_REVIEW_REPORT.json`, `missing_notebooks_list.json`)
- [x] Keep a repeatable audit process (scripts + saved audit artifacts)

## Coverage Implementation (All Courses)

- [x] Course 01: Fill missing code-able activities with notebooks under `examples/`
- [x] Course 02: Fill missing code-able activities with notebooks under `examples/`
- [x] Course 03: Fill missing code-able activities with notebooks under `examples/`
- [x] Course 04: Fill missing code-able activities with notebooks under `examples/`
- [x] Course 05: Fill missing code-able activities with notebooks under `examples/`
- [x] Course 06: Add notebooks for code-able ethics activities (bias, privacy, fairness, XAI) and supporting materials
- [x] Course 07: Fill NLP practical activities with notebooks under `examples/`
- [x] Course 08: Fill deep learning practical activities with notebooks under `examples/`
- [x] Course 09: Fill RL practical activities with notebooks under `examples/`
- [x] Course 10: Fill generative AI practical activities with notebooks under `examples/`
- [x] Course 11: Fill deployment/MLOps practical activities with notebooks under `examples/`
- [x] Course 12: Fill graduation project practical activities with notebooks under `examples/`

## Notebook Quality Guidelines (Applies to Every New Notebook)

- [x] Each notebook contains:
  - [x] Title matching the practical activity
  - [x] Learning objectives
  - [x] Prerequisites
  - [x] “Official Structure Reference” pointing to `DETAILED_UNIT_DESCRIPTIONS.md`
  - [x] Runnable, topic-appropriate example code (where code-able)
- [x] Notebook formatting renders correctly in Jupyter (proper newline handling in cell sources)
- [x] Avoid empty notebooks (`cells: []`)
- [x] Avoid placeholder-only notebooks (prints-only scaffolds without real examples)

## Verification & Reporting

- [x] Run a coverage audit (file presence + activity matching)
- [x] Produce audit artifacts:
  - [x] `GUIDELINES_AUDIT.json`
  - [x] `100_PERCENT_COVERAGE_COMPLETE.md`
  - [x] (Optional) `COURSE_03_06_VERIFICATION_COMPLETE.md`
- [x] Confirm:
  - [x] Missing activity matches: 0
  - [x] Empty notebooks: 0
  - [x] Placeholder notebooks: 0

## Cleanup

- [x] Remove duplicates if any exist (keep the most complete notebook per topic)
- [x] Ensure folder naming is consistent and navigable

## Version Control (Professional)

- [ ] Stage changes in logical groups where feasible
- [ ] Commit with conventional commit messages (e.g., `feat:`, `fix:`, `docs:`)
- [ ] Ensure `git status` is clean after commits

