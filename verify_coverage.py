#!/usr/bin/env python3
"""
Systematic Content Coverage Verification
Compares official requirements with actual content
"""
import os
import re
from pathlib import Path

def extract_official_requirements():
    """Extract all practical content requirements from DETAILED_UNIT_DESCRIPTIONS.md"""
    with open('DETAILED_UNIT_DESCRIPTIONS.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    courses = {}
    current_course = None
    current_unit = None
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Course headers
        if line.startswith('## 📘 COURSE'):
            match = re.search(r'COURSE (\d+):', line)
            if match:
                current_course = int(match.group(1))
                courses[current_course] = {'units': {}}
        # Unit headers
        elif line.startswith('#### 📖 Unit') and current_course:
            match = re.search(r'Unit (\d+):', line)
            if match:
                current_unit = int(match.group(1))
                courses[current_course]['units'][current_unit] = {'practical': [], 'theory': []}
        # Practical Content section
        elif '**Practical Content:**' in line and current_course and current_unit:
            for j in range(i+1, min(i+30, len(lines))):
                next_line = lines[j].strip()
                if next_line.startswith('---') or (next_line.startswith('####') and 'Unit' in next_line) or (next_line.startswith('##') and 'COURSE' in next_line):
                    break
                if next_line.startswith('-') and next_line:
                    courses[current_course]['units'][current_unit]['practical'].append(next_line.strip('- ').strip())
    
    return courses

def check_course_content(course_num):
    """Check what notebooks/exercises exist for a course"""
    course_dir = f"Course {course_num:02d}"
    if not os.path.exists(course_dir):
        return {'exists': False, 'units': {}}
    
    result = {'exists': True, 'units': {}}
    
    # Find unit folders
    for item in os.listdir(course_dir):
        unit_path = os.path.join(course_dir, item)
        if os.path.isdir(unit_path) and item.startswith('unit'):
            # Extract unit number
            match = re.search(r'unit(\d+)', item)
            if match:
                unit_num = int(match.group(1))
                result['units'][unit_num] = {
                    'notebooks': [],
                    'exercises': []
                }
                
                # Find notebooks
                examples_dir = os.path.join(unit_path, 'examples')
                if os.path.exists(examples_dir):
                    for nb in os.listdir(examples_dir):
                        if nb.endswith('.ipynb'):
                            result['units'][unit_num]['notebooks'].append(nb)
                
                # Find exercises
                exercises_dir = os.path.join(unit_path, 'exercises')
                if os.path.exists(exercises_dir):
                    for ex in os.listdir(exercises_dir):
                        if ex.endswith('.ipynb') or ex.endswith('.py'):
                            result['units'][unit_num]['exercises'].append(ex)
    
    return result

def main():
    print("🔍 SYSTEMATIC CONTENT COVERAGE VERIFICATION")
    print("=" * 60)
    print()
    
    # Extract official requirements
    requirements = extract_official_requirements()
    
    # Check each course
    gaps = {}
    
    for course_num in sorted(requirements.keys()):
        print(f"\n{'='*60}")
        print(f"COURSE {course_num:02d}")
        print(f"{'='*60}")
        
        actual = check_course_content(course_num)
        gaps[course_num] = {'missing': [], 'partial': []}
        
        if not actual['exists']:
            print(f"❌ Course folder not found!")
            gaps[course_num]['missing'].append("ENTIRE COURSE STRUCTURE")
            continue
        
        print(f"✅ Course folder exists")
        print(f"   Official units: {len(requirements[course_num]['units'])}")
        print(f"   Actual units found: {len(actual['units'])}")
        
        # Check each unit
        for unit_num in sorted(requirements[course_num]['units'].keys()):
            print(f"\n  Unit {unit_num}:")
            req = requirements[course_num]['units'][unit_num]['practical']
            
            if unit_num not in actual['units']:
                print(f"    ❌ Unit folder not found!")
                gaps[course_num]['missing'].append(f"Unit {unit_num}: ENTIRE UNIT")
                continue
            
            unit_actual = actual['units'][unit_num]
            notebooks = [nb.lower() for nb in unit_actual['notebooks']]
            exercises = [ex.lower() for ex in unit_actual['exercises']]
            
            print(f"    ✅ Unit folder exists")
            print(f"    📝 Notebooks: {len(unit_actual['notebooks'])}")
            print(f"    ✏️  Exercises: {len(unit_actual['exercises'])}")
            print(f"    📋 Required practical activities: {len(req)}")
            
            # Check if requirements are covered (basic keyword matching)
            for req_item in req:
                keywords = re.findall(r'\b\w+\b', req_item.lower())
                found = False
                for keyword in keywords[:3]:  # Check first 3 keywords
                    if any(keyword in nb for nb in notebooks) or any(keyword in ex for ex in exercises):
                        found = True
                        break
                
                if not found and len(keywords) > 0:
                    print(f"      ⚠️  May be missing: {req_item[:60]}...")
                    gaps[course_num]['partial'].append(f"Unit {unit_num}: {req_item}")
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY OF GAPS")
    print(f"{'='*60}\n")
    
    for course_num in sorted(gaps.keys()):
        if gaps[course_num]['missing'] or gaps[course_num]['partial']:
            print(f"Course {course_num:02d}:")
            if gaps[course_num]['missing']:
                print(f"  ❌ Critical gaps: {len(gaps[course_num]['missing'])}")
            if gaps[course_num]['partial']:
                print(f"  ⚠️  Potential gaps: {len(gaps[course_num]['partial'])}")
        else:
            print(f"Course {course_num:02d}: ✅ Looks complete")

if __name__ == '__main__':
    main()
