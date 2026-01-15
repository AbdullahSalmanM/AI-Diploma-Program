#!/usr/bin/env python3
"""
Comprehensive Alignment Review
Checks if all content aligns with DETAILED_UNIT_DESCRIPTIONS.md
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent
DETAILED_DESC_FILE = BASE_DIR / "DETAILED_UNIT_DESCRIPTIONS.md"

def extract_practical_requirements():
    """Extract all practical content requirements from DETAILED_UNIT_DESCRIPTIONS.md"""
    with open(DETAILED_DESC_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    courses = {}
    current_course = None
    current_unit = None
    
    # Find course and unit sections
    course_pattern = r'## 📘 COURSE (\d+):'
    unit_pattern = r'#### 📖 Unit (\d+): (.+?)\((\d+) hours'
    practical_pattern = r'\*\*Practical Content:\*\*\s*\n(.*?)(?=\n---|\n####|$)'
    
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for course
        course_match = re.search(course_pattern, line)
        if course_match:
            course_num = int(course_match.group(1))
            current_course = course_num
            courses[course_num] = {'units': {}}
        
        # Check for unit
        unit_match = re.search(unit_pattern, line)
        if unit_match and current_course:
            unit_num = int(unit_match.group(1))
            unit_name = unit_match.group(2).strip()
            current_unit = unit_num
            courses[current_course]['units'][unit_num] = {
                'name': unit_name,
                'practical_activities': []
            }
        
        # Check for practical content section
        if line.strip() == '**Practical Content:**' and current_course and current_unit:
            # Collect practical activities
            i += 1
            activities = []
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('- '):
                    activities.append(next_line[2:].strip())
                elif next_line.startswith('---') or next_line.startswith('####'):
                    break
                elif next_line and not next_line.startswith('**'):
                    # Continuation of previous activity
                    if activities:
                        activities[-1] += ' ' + next_line
                i += 1
            
            courses[current_course]['units'][current_unit]['practical_activities'] = activities
            continue
        
        i += 1
    
    return courses

def get_existing_notebooks(course_num, unit_num):
    """Get list of existing notebooks for a course unit"""
    course_dir = BASE_DIR / f"Course {course_num:02d}"
    if not course_dir.exists():
        return []
    
    notebooks = []
    # Find unit folder
    unit_folders = [d for d in course_dir.iterdir() 
                    if d.is_dir() and d.name.startswith(f'unit{unit_num}')]
    
    for unit_folder in unit_folders:
        examples_dir = unit_folder / 'examples'
        if examples_dir.exists():
            for nb_file in examples_dir.glob('*.ipynb'):
                notebooks.append(nb_file.name)
    
    return notebooks

def keyword_match(activity, notebook_name):
    """Check if notebook name matches activity keywords"""
    activity_lower = activity.lower()
    notebook_lower = notebook_name.lower().replace('_', ' ').replace('-', ' ')
    
    # Extract key terms from activity
    key_terms = []
    common_terms = {
        'word2vec': ['word2vec', 'word embeddings', 'word embedding'],
        'bert': ['bert', 'fine-tuning', 'fine tune'],
        'seq2seq': ['seq2seq', 'sequence to sequence', 'sequence-to-sequence'],
        'gpt': ['gpt', 'openai', 'text generation'],
        'ner': ['ner', 'named entity', 'entity recognition'],
        'pos': ['pos', 'part of speech', 'tagging'],
        'rdf': ['rdf', 'sparql', 'knowledge graph'],
        'bayesian': ['bayesian', 'bayes', 'network'],
        'hmm': ['hmm', 'hidden markov', 'viterbi'],
        'mdp': ['mdp', 'markov decision', 'value iteration'],
        'svd': ['svd', 'singular value'],
        'tsne': ['tsne', 't-sne', 'visualization'],
        'ridge': ['ridge', 'lasso', 'regularization'],
        'svr': ['svr', 'support vector regression'],
        'random forest': ['random forest', 'rf'],
        'naive bayes': ['naive bayes', 'nb'],
        'ensemble': ['ensemble', 'bagging', 'boosting'],
        'lda': ['lda', 'linear discriminant'],
        'umap': ['umap'],
        'cudf': ['cudf', 'gpu'],
        'perceptron': ['perceptron', 'mlp'],
        'tensorflow': ['tensorflow', 'tf'],
        'pytorch': ['pytorch', 'torch'],
        'flask': ['flask'],
        'fastapi': ['fastapi'],
        'docker': ['docker', 'container'],
        'kubernetes': ['kubernetes', 'k8s'],
        'aws': ['aws', 'sagemaker'],
        'azure': ['azure'],
        'gcp': ['gcp', 'vertex ai']
    }
    
    for term, variants in common_terms.items():
        if any(v in activity_lower for v in variants):
            key_terms.extend(variants)
    
    # Check if notebook matches any key terms
    if key_terms:
        return any(term in notebook_lower for term in key_terms)
    
    # Fallback: check for common words
    activity_words = set(re.findall(r'\b\w+\b', activity_lower))
    notebook_words = set(re.findall(r'\b\w+\b', notebook_lower))
    common_words = activity_words.intersection(notebook_words)
    
    # If at least 2 significant words match
    significant_words = [w for w in common_words if len(w) > 4]
    return len(significant_words) >= 2

def review_alignment():
    """Main review function"""
    print("=" * 80)
    print("COMPREHENSIVE ALIGNMENT REVIEW")
    print("=" * 80)
    print()
    
    # Extract requirements
    print("📚 Extracting requirements from DETAILED_UNIT_DESCRIPTIONS.md...")
    requirements = extract_practical_requirements()
    print(f"✅ Found {len(requirements)} courses")
    print()
    
    # Review each course
    alignment_report = {}
    total_activities = 0
    total_covered = 0
    
    for course_num in sorted(requirements.keys()):
        course_info = requirements[course_num]
        print(f"🔍 Reviewing Course {course_num:02d}...")
        
        course_report = {
            'units': {},
            'total_activities': 0,
            'covered_activities': 0,
            'missing_activities': []
        }
        
        for unit_num in sorted(course_info['units'].keys()):
            unit_info = course_info['units'][unit_num]
            activities = unit_info['practical_activities']
            existing_notebooks = get_existing_notebooks(course_num, unit_num)
            
            course_report['total_activities'] += len(activities)
            total_activities += len(activities)
            
            unit_report = {
                'unit_name': unit_info['name'],
                'required_activities': activities,
                'existing_notebooks': existing_notebooks,
                'covered': [],
                'missing': []
            }
            
            # Check coverage
            for activity in activities:
                covered = False
                for notebook in existing_notebooks:
                    if keyword_match(activity, notebook):
                        unit_report['covered'].append(activity)
                        course_report['covered_activities'] += 1
                        total_covered += 1
                        covered = True
                        break
                
                if not covered:
                    unit_report['missing'].append(activity)
                    course_report['missing_activities'].append(f"Unit {unit_num}: {activity}")
            
            course_report['units'][unit_num] = unit_report
            
            # Print unit summary
            coverage_pct = (len(unit_report['covered']) / len(activities) * 100) if activities else 100
            status = "✅" if coverage_pct == 100 else "⚠️"
            print(f"   {status} Unit {unit_num}: {len(unit_report['covered'])}/{len(activities)} activities covered ({coverage_pct:.0f}%)")
            if unit_report['missing']:
                for missing in unit_report['missing'][:2]:  # Show first 2
                    print(f"      ⚠️  Missing: {missing[:60]}...")
        
        alignment_report[course_num] = course_report
        
        # Course summary
        course_coverage = (course_report['covered_activities'] / course_report['total_activities'] * 100) if course_report['total_activities'] > 0 else 100
        status = "✅" if course_coverage == 100 else "⚠️"
        print(f"   {status} Course {course_num:02d}: {course_report['covered_activities']}/{course_report['total_activities']} activities ({course_coverage:.0f}%)")
        print()
    
    # Overall summary
    print("=" * 80)
    print("ALIGNMENT REVIEW SUMMARY")
    print("=" * 80)
    print()
    
    overall_coverage = (total_covered / total_activities * 100) if total_activities > 0 else 100
    print(f"📊 Overall Statistics:")
    print(f"   Total Practical Activities: {total_activities}")
    print(f"   Activities Covered: {total_covered}")
    print(f"   Overall Coverage: {overall_coverage:.1f}%")
    print()
    
    # Courses with issues
    print("⚠️  Courses with Missing Activities:")
    issues_found = False
    for course_num, report in alignment_report.items():
        if report['missing_activities']:
            issues_found = True
            print(f"\n   Course {course_num:02d} ({len(report['missing_activities'])} missing):")
            for missing in report['missing_activities'][:3]:  # Show first 3
                print(f"      - {missing}")
            if len(report['missing_activities']) > 3:
                print(f"      ... and {len(report['missing_activities']) - 3} more")
    
    if not issues_found:
        print("   ✅ No missing activities found!")
    
    print()
    print("=" * 80)
    print("✅ Review Complete!")
    print("=" * 80)
    
    # Save detailed report
    report_file = BASE_DIR / "ALIGNMENT_REVIEW_REPORT.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(alignment_report, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: {report_file}")
    
    return alignment_report

if __name__ == "__main__":
    review_alignment()
