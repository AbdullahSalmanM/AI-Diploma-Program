# Quiz Structure Analysis Across All Courses

## Current Structure Comparison

### ✅ Standard Structure (Courses 02 & 03)
- **Course 02**: All 6 quizzes in main `QUIZZES/` folder
  - `Quiz_00_Python_Libraries.md`
  - `Quiz_01_Search_Algorithms.md`
  - `Quiz_02_Knowledge_Representation.md`
  - `Quiz_03_Uncertainty.md`
  - `Quiz_04_Optimization.md`
  - `Quiz_05_ML_Models.md`

- **Course 03**: All 5 quizzes in main `QUIZZES/` folder
  - `Quiz_01_Linear_Algebra.md`
  - `Quiz_02_Calculus.md`
  - `Quiz_03_Optimization_Statistics.md`
  - `Quiz_04_Dimensionality_Reduction.md`
  - `Quiz_05_Probabilities_Inference.md`

### ❌ Inconsistent Structure (Courses 04, 05, 06)

#### Course 04
- **Main QUIZZES folder**: 1 quiz (`quiz_01_data_processing.md`)
- **Unit folders**: 5 quizzes (one per unit)
  - `unit1/quizzes/quiz_01.md`
  - `unit2/quizzes/quiz_02.md`
  - `unit3/quizzes/quiz_03.md`
  - `unit4/quizzes/quiz_04.md`
  - `unit5/quizzes/quiz_05.md`
- **Total**: 6 quizzes (1 in main, 5 in units) - **INCONSISTENT**

#### Course 05
- **Main QUIZZES folder**: 1 quiz (`Quiz_01_Introduction_Data_Science.md`)
- **Unit folders**: 5 quizzes (one per unit)
  - `unit1-introduction/quizzes/quiz_01.md`
  - `unit2-cleaning/quizzes/quiz_02.md`
  - `unit3-visualization/quizzes/quiz_03.md`
  - `unit4-ml-intro/quizzes/quiz_04.md`
  - `unit5-scaling/quizzes/quiz_05.md`
- **Total**: 6 quizzes (1 in main, 5 in units) - **INCONSISTENT**
- **Note**: The main quiz appears to be a duplicate of `unit1/quizzes/quiz_01.md`

#### Course 06
- **Main QUIZZES folder**: 0 quizzes (only `quiz_summary.md` and `README.md`)
- **Unit folders**: 5 quizzes (one per unit)
  - `unit1-ethics-foundations/quizzes/quiz_01.md`
  - `unit2-bias-justice/quizzes/quiz_02.md`
  - `unit3-privacy-security/quizzes/quiz_03.md`
  - `unit4-transparency-accountability/quizzes/quiz_04.md`
  - `unit5-governance-regulations/quizzes/quiz_05.md`
- **Total**: 5 quizzes (0 in main, 5 in units) - **INCONSISTENT**

## Recommended Standard Structure

**All quizzes should be in the main `QUIZZES/` folder** for consistency with Courses 02 and 03.

### Benefits:
1. **Consistency**: Students know where to find all quizzes
2. **Centralized**: Easier to manage and update
3. **Navigation**: Clear structure across all courses
4. **Maintenance**: Single location for quiz-related files

## Action Required

### Course 04
- Move 5 unit quizzes to main `QUIZZES/` folder
- Remove duplicate `quiz_01_data_processing.md` if it matches unit1 quiz
- Rename to match naming convention: `Quiz_01_*.md`, `Quiz_02_*.md`, etc.

### Course 05
- Move 5 unit quizzes to main `QUIZZES/` folder
- Remove duplicate `Quiz_01_Introduction_Data_Science.md` if it matches unit1 quiz
- Rename to match naming convention

### Course 06
- Move 5 unit quizzes to main `QUIZZES/` folder
- Rename to match naming convention: `Quiz_01_*.md`, `Quiz_02_*.md`, etc.

## Naming Convention

Based on Courses 02 and 03:
- Format: `Quiz_XX_Topic_Name.md` (with leading zeros for numbers < 10)
- Example: `Quiz_01_Introduction_Data_Science.md`
