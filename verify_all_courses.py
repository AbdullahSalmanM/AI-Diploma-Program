#!/usr/bin/env python3
"""
Systematic Verification Script
Verifies all 12 courses against DETAILED_UNIT_DESCRIPTIONS.md
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

# Paths
BASE_DIR = Path(__file__).parent
DETAILED_DESC_FILE = BASE_DIR / "DETAILED_UNIT_DESCRIPTIONS.md"
COURSES_DIR = BASE_DIR

def extract_course_structure():
    """Extract all courses and units from DETAILED_UNIT_DESCRIPTIONS.md"""
    with open(DETAILED_DESC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    courses = {}
    current_course = None
    
    # Find course headers - handle both "COURSE 1" and "COURSE 01" formats
    course_pattern = r'## 📘 COURSE (\d+): (.+)'
    unit_pattern = r'#### 📖 Unit (\d+): (.+?)\((\d+) hours'
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Check for course header
        course_match = re.search(course_pattern, line)
        if course_match:
            course_num = int(course_match.group(1))
            course_name = course_match.group(2).strip()
            courses[course_num] = {
                'name': course_name,
                'units': {}
            }
            current_course = course_num
        
        # Check for unit header
        unit_match = re.search(unit_pattern, line)
        if unit_match and current_course:
            unit_num = int(unit_match.group(1))
            unit_name = unit_match.group(2).strip()
            hours = unit_match.group(3)
            courses[current_course]['units'][unit_num] = {
                'name': unit_name,
                'hours': hours
            }
    
    return courses

def extract_practical_content(course_num, unit_num):
    """Extract practical content requirements from DETAILED_UNIT_DESCRIPTIONS.md"""
    with open(DETAILED_DESC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the course section
    course_pattern = rf'^## 📘 COURSE {course_num}:.*?\n(.*?)(?=^## 📘|$)'
    course_match = re.search(course_pattern, content, re.MULTILINE | re.DOTALL)
    if not course_match:
        return []
    
    course_content = course_match.group(1)
    
    # Find the unit section
    unit_pattern = rf'^#### 📖 Unit {unit_num}:.*?\n(.*?)(?=^#### 📖|^---|$)'
    unit_match = re.search(unit_pattern, course_content, re.MULTILINE | re.DOTALL)
    if not unit_match:
        return []
    
    unit_content = unit_match.group(1)
    
    # Extract practical content
    practical_pattern = r'\*\*Practical Content:\*\*\s*\n(.*?)(?=---|$)'
    practical_match = re.search(practical_pattern, unit_content, re.MULTILINE | re.DOTALL)
    if not practical_match:
        return []
    
    practical_text = practical_match.group(1)
    # Extract bullet points
    activities = []
    for line in practical_text.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            activities.append(line[2:].strip())
    
    return activities

def check_course_structure(course_num):
    """Check if course has proper structure"""
    course_dir = COURSES_DIR / f"Course {course_num:02d}"
    
    if not course_dir.exists():
        return {
            'exists': False,
            'units': [],
            'notebooks': [],
            'exercises': [],
            'readmes': []
        }
    
    # Find units
    units = []
    for item in course_dir.iterdir():
        if item.is_dir() and item.name.startswith('unit'):
            units.append(item.name)
    
    # Find notebooks
    notebooks = []
    exercises = []
    readmes = []
    
    for root, dirs, files in os.walk(course_dir):
        root_path = Path(root)
        for file in files:
            if file.endswith('.ipynb'):
                # Check if path contains 'examples' or 'exercises'
                root_str = str(root_path)
                if 'examples' in root_str:
                    notebooks.append(str(root_path / file))
                elif 'exercises' in root_str:
                    exercises.append(str(root_path / file))
            elif file == 'README.md':
                readmes.append(str(root_path / file))
    
    return {
        'exists': True,
        'units': sorted(units),
        'notebooks': notebooks,
        'exercises': exercises,
        'readmes': readmes
    }

def main():
    """Main verification function"""
    print("=" * 80)
    print("SYSTEMATIC VERIFICATION OF ALL 12 COURSES")
    print("=" * 80)
    print()
    
    # Extract structure from DETAILED_UNIT_DESCRIPTIONS.md
    print("📚 Extracting structure from DETAILED_UNIT_DESCRIPTIONS.md...")
    expected_structure = extract_course_structure()
    
    print(f"✅ Found {len(expected_structure)} courses")
    for course_num, course_info in sorted(expected_structure.items()):
        print(f"   Course {course_num:02d}: {len(course_info['units'])} units")
    print()
    
    # Verify each course
    verification_report = {}
    
    for course_num in range(1, 13):
        print(f"🔍 Verifying Course {course_num:02d}...")
        
        expected_units = expected_structure.get(course_num, {}).get('units', {})
        actual_structure = check_course_structure(course_num)
        
        # Count expected vs actual units
        expected_unit_count = len(expected_units)
        actual_unit_count = len(actual_structure['units'])
        
        verification_report[course_num] = {
            'expected_units': expected_unit_count,
            'actual_units': actual_unit_count,
            'notebooks': len(actual_structure['notebooks']),
            'exercises': len(actual_structure['exercises']),
            'readmes': len(actual_structure['readmes']),
            'structure': actual_structure
        }
        
        status = "✅" if actual_unit_count == expected_unit_count else "⚠️"
        print(f"   {status} Units: {actual_unit_count}/{expected_unit_count}")
        print(f"   📓 Notebooks: {len(actual_structure['notebooks'])}")
        print(f"   📝 Exercises: {len(actual_structure['exercises'])}")
        print(f"   📄 READMEs: {len(actual_structure['readmes'])}")
        print()
    
    # Summary
    print("=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    print()
    
    total_expected_units = sum(r['expected_units'] for r in verification_report.values())
    total_actual_units = sum(r['actual_units'] for r in verification_report.values())
    total_notebooks = sum(r['notebooks'] for r in verification_report.values())
    total_exercises = sum(r['exercises'] for r in verification_report.values())
    
    print(f"📊 Overall Statistics:")
    print(f"   Expected Units: {total_expected_units}")
    print(f"   Actual Units: {total_actual_units}")
    print(f"   Total Notebooks: {total_notebooks}")
    print(f"   Total Exercises: {total_exercises}")
    print()
    
    # Issues
    print("⚠️  Issues Found:")
    issues = []
    for course_num, report in verification_report.items():
        if report['expected_units'] != report['actual_units']:
            issues.append(f"Course {course_num:02d}: Expected {report['expected_units']} units, found {report['actual_units']}")
    
    if not issues:
        print("   ✅ No structural issues found!")
    else:
        for issue in issues:
            print(f"   {issue}")
    
    print()
    print("=" * 80)
    print("✅ Verification Complete!")
    print("=" * 80)
    
    # Save report
    report_file = BASE_DIR / "VERIFICATION_REPORT_ALL_COURSES.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(verification_report, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: {report_file}")

if __name__ == "__main__":
    main()

