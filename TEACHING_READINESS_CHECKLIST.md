# Teaching Readiness Checklist
## Complete Notebook Audit & Coverage Verification

**Date Started:** [To be filled]  
**Target:** All notebooks execute without errors + 100% topic coverage per `DETAILED_UNIT_DESCRIPTIONS.md`

---

## Phase A: Setup & Preparation

### Environment Setup
- [ ] Confirm Python environment (venv/conda) is active
- [ ] Install all dependencies from `requirements.txt`
- [ ] Verify Jupyter is installed and working
- [ ] Record Python version: `python --version`
- [ ] Record key package versions (numpy, pandas, tensorflow, torch, etc.)
- [ ] Record Jupyter kernel name being used
- [ ] Test basic notebook execution with a simple test notebook

### Tooling Setup
- [ ] Create `tools/` directory if it doesn't exist
- [ ] Create `artifacts/` directory for execution results
- [ ] Ensure `artifacts/executed/` exists for saved executed notebooks
- [ ] Ensure `artifacts/logs/` exists for execution logs

---

## Phase B: Static Coverage Analysis

### Parse Curriculum Requirements
- [ ] Parse `DETAILED_UNIT_DESCRIPTIONS.md` into structured format
- [ ] Extract all Course → Unit → Topic mappings
- [ ] Extract all practical activities per unit
- [ ] Create structured JSON/YAML representation of curriculum

### Repository Structure Verification
- [ ] Verify all 12 courses exist (Course 01 through Course 12)
- [ ] For each course, verify unit directories exist
- [ ] Check for unit README files (unit-level documentation)
- [ ] Verify expected notebook locations:
  - [ ] `unit*/examples/` directories exist
  - [ ] `unit*/exercises/` directories exist (where applicable)
  - [ ] Course-specific structures (e.g., `Course 02/NOTEBOOKS/`)
- [ ] Count total notebooks per course/unit

### Coverage Mapping
- [ ] Generate coverage map: curriculum topics → notebook files
- [ ] Identify missing notebooks (topics without corresponding notebooks)
- [ ] Identify orphaned notebooks (notebooks not matching curriculum topics)
- [ ] Create `COVERAGE_MAP_REPORT.md` with findings

---

## Phase C: Notebook Execution Audit

### Execution Runner Setup
- [ ] Create `tools/notebook_runner.py` script
- [ ] Implement notebook discovery (find all `.ipynb` files)
- [ ] Implement execution with timeout (e.g., 5 minutes per notebook)
- [ ] Implement error capture and logging
- [ ] Implement executed notebook saving to `artifacts/executed/`
- [ ] Test runner on a small subset (e.g., 5 notebooks)

### Full Execution Run
- [ ] Execute all notebooks in Course 01
- [ ] Execute all notebooks in Course 02
- [ ] Execute all notebooks in Course 03
- [ ] Execute all notebooks in Course 04
- [ ] Execute all notebooks in Course 05
- [ ] Execute all notebooks in Course 06
- [ ] Execute all notebooks in Course 07
- [ ] Execute all notebooks in Course 08
- [ ] Execute all notebooks in Course 09
- [ ] Execute all notebooks in Course 10
- [ ] Execute all notebooks in Course 11
- [ ] Execute all notebooks in Course 12

### Execution Report Generation
- [ ] Generate `NOTEBOOK_EXECUTION_REPORT.md` (human-readable)
- [ ] Generate `NOTEBOOK_EXECUTION_REPORT.json` (machine-readable)
- [ ] Include for each notebook:
  - [ ] Pass/Fail status
  - [ ] Execution time
  - [ ] Error message (if failed)
  - [ ] Error traceback (if failed)
  - [ ] File path
  - [ ] Course/Unit classification

---

## Phase D: Issue Triage & Fixes

### Error Analysis
- [ ] Categorize failures by error type:
  - [ ] Missing imports
  - [ ] Broken file paths
  - [ ] Missing datasets/files
  - [ ] Version incompatibilities
  - [ ] API key/authentication issues
  - [ ] Timeout issues
  - [ ] Other runtime errors
- [ ] Prioritize fixes (critical → nice-to-have)

### Fix Implementation
- [ ] Fix missing imports (add to cells or requirements.txt)
- [ ] Fix broken file paths (use relative paths, add setup cells)
- [ ] Fix missing datasets (add download instructions or mock data)
- [ ] Fix version incompatibilities (update code or pin versions)
- [ ] Handle API key issues (add clear instructions or skip gracefully)
- [ ] Fix timeout issues (optimize code or increase timeout)
- [ ] Fix other runtime errors

### Re-execution After Fixes
- [ ] Re-run execution on fixed notebooks
- [ ] Verify fixes resolved issues
- [ ] Update execution reports with new results

---

## Phase E: Final Verification

### Coverage Verification
- [ ] Verify all curriculum topics have corresponding notebooks
- [ ] Verify all notebooks align with curriculum topics
- [ ] Check unit READMEs match curriculum descriptions
- [ ] Generate final coverage report

### Execution Verification
- [ ] Confirm 0 execution failures (or document acceptable failures)
- [ ] Review execution times (flag any unusually slow notebooks)
- [ ] Verify all executed notebooks saved correctly

### Documentation
- [ ] Update `TEACHING_READINESS_REPORT.md` with final status
- [ ] Include summary statistics:
  - [ ] Total notebooks executed
  - [ ] Pass rate
  - [ ] Coverage percentage
  - [ ] Known issues/limitations
- [ ] Create quick reference guide for common issues

---

## Phase F: Version Control & Sign-off

### Git Commit Strategy
- [ ] Stage notebook fixes in logical groups
- [ ] Commit with conventional commits:
  - [ ] `chore: add notebook execution runner`
  - [ ] `fix: [notebook name] - [issue description]`
  - [ ] `docs: add teaching readiness reports`
- [ ] Ensure commit messages are clear and descriptive

### Final Sign-off
- [ ] Review all reports one final time
- [ ] Confirm readiness for teaching
- [ ] Document any known limitations or workarounds
- [ ] Mark checklist as complete

---

## Summary Statistics

**Total Notebooks:** [To be filled]  
**Passed:** [To be filled]  
**Failed:** [To be filled]  
**Pass Rate:** [To be filled]%  
**Coverage:** [To be filled]%  
**Status:** ⏳ In Progress / ✅ Complete / ❌ Issues Found

---

## Notes & Known Issues

[Space for documenting any issues, workarounds, or special considerations]

---

**Last Updated:** [Date]
