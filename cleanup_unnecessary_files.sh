#!/bin/bash
# Cleanup script to remove unnecessary .md files

echo "Starting cleanup of unnecessary files..."
echo ""

# Root level files to delete
ROOT_FILES=(
    "ALL_COURSES_CONFLICT_CHECK.md"
    "ALL_COURSES_CONSISTENCY_REPORT.md"
    "ALL_COURSES_FIXES_COMPLETE.md"
    "BEGINNER_GUIDES_STATUS.md"
    "CLEANUP_PLAN.md"
    "CLEANUP_SUMMARY.md"
    "COMPREHENSIVE_NOTEBOOK_REVIEW.md"
    "CONFLICT_CHECK_REPORT.md"
    "CONTENT_DEVELOPMENT_STATUS.md"
    "COURSE_01_COMPARISON.md"
    "COURSE_04_OUTPUT_ANALYSIS.md"
    "COURSE_04_QUIZ_ANALYSIS.md"
    "COURSE_06_STATUS.md"
    "COURSE_MAP.md"
    "COURSE_SUMMARIES_COMPLETE.md"
    "COURSE_SUMMARIES_CREATED.md"
    "COURSE_SUMMARY_FIXES.md"
    "DEPLOYMENT_SUMMARY.md"
    "EMPTY_FOLDERS_FIXED.md"
    "EMPTY_QUIZ_FOLDERS_FIXED.md"
    "FINAL_FIXES_SUMMARY.md"
    "FINAL_STUDENT_READINESS_REPORT.md"
    "GUIDE_COMPARISON_ANALYSIS.md"
    "GUIDE_COMPARISON_AND_RECOMMENDATION.md"
    "GUIDE_MERGE_SUMMARY.md"
    "GUIDE_USAGE_RECOMMENDATION.md"
    "GUIDES_VS_SOLUTIONS_ANALYSIS.md"
    "HONEST_VERIFICATION_REPORT.md"
    "NOTEBOOK_FIXES_SUMMARY.md"
    "PLAN_COMPARISON.md"
    "PROJECT_BEGINNER_GUIDES_SUMMARY.md"
    "PROJECT_COURSE_CONNECTIONS.md"
    "PROJECT_REAL_WORLD_VERIFICATION.md"
    "PROJECT_SOLUTIONS_SUMMARY.md"
    "PROJECT_STUDENT_TEMPLATE.md"
    "QUIZ_STANDARDIZATION_COMPLETE.md"
    "QUIZ_STRUCTURE_ANALYSIS.md"
    "README_VS_PROJECT_GUIDE_ANALYSIS.md"
    "REQUIREMENTS_VERIFICATION_REPORT.md"
    "SHOULD_WE_KEEP_BOTH_GUIDES.md"
    "SOLUTIONS_STATUS.md"
    "STRUCTURE_COMPARISON.md"
    "STUDENT_CONVENIENCE_REPORT.md"
    "STUDENT_REPOSITORY_CLEANUP.md"
    "WHAT_NEXT.md"
    "BEGINNER_PROJECT_GUIDE.md"
)

# Delete root level files
for file in "${ROOT_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Deleting: $file"
        rm "$file"
    fi
done

# Delete course-level meta files
echo ""
echo "Deleting course-level meta files..."
find "Course 0"* -name "COURSE_SUMMARY.md" -type f -delete
find "Course 0"* -path "*/META/*.md" -type f -delete

# Delete Course 04 specific meta files
COURSE04_FILES=(
    "Course 04/COURSE_04_COMPLETE_STATUS.md"
    "Course 04/NOTEBOOK_ANALYSIS.md"
    "Course 04/NOTEBOOK_COVERAGE_REPORT.md"
    "Course 04/EXERCISE_COVERAGE_REPORT.md"
    "Course 04/REQUIREMENTS_VERIFICATION_REPORT.md"
    "Course 04/NEXT_STEPS.md"
    "Course 04/ASSESSMENTS/ASSESSMENT_SUMMARY.md"
    "Course 04/unit1-data-processing/TESTING_REPORT.md"
)

for file in "${COURSE04_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Deleting: $file"
        rm "$file"
    fi
done

echo ""
echo "Cleanup complete!"
echo "Files deleted. Review with: git status"
