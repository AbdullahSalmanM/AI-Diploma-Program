#!/usr/bin/env python3
"""
Merge Implementation_Guide.md and BEGINNER_GUIDE.md into comprehensive PROJECT_GUIDE.md
"""

import re
from pathlib import Path

def extract_sections(content, guide_type):
    """Extract key sections from guide"""
    sections = {
        'real_world': '',
        'quick_start': '',
        'tutorial': '',
        'course_connections': '',
        'troubleshooting': ''
    }
    
    # Extract real-world application
    real_world_match = re.search(r'## 🎯 Real-World Application.*?(?=##|\Z)', content, re.DOTALL)
    if real_world_match:
        sections['real_world'] = real_world_match.group(0).strip()
    
    # Extract quick start (from Implementation Guide)
    if guide_type == 'implementation':
        quick_start_match = re.search(r'## Step-by-Step Implementation.*?(?=##|\Z)', content, re.DOTALL)
        if quick_start_match:
            sections['quick_start'] = quick_start_match.group(0).strip()
    
    # Extract tutorial (from Beginner Guide)
    if guide_type == 'beginner':
        tutorial_match = re.search(r'## 📚 Step-by-Step Guide.*?(?=##|\Z)', content, re.DOTALL)
        if tutorial_match:
            sections['tutorial'] = tutorial_match.group(0).strip()
    
    # Extract course connections
    course_match = re.search(r'📖 Course Connection.*?(?=\n\n|\Z)', content, re.DOTALL)
    if course_match:
        sections['course_connections'] = course_match.group(0).strip()
    
    # Extract troubleshooting
    trouble_match = re.search(r'## 🐛 Troubleshooting.*?(?=##|\Z)', content, re.DOTALL)
    if trouble_match:
        sections['troubleshooting'] = trouble_match.group(0).strip()
    
    return sections

def create_merged_guide(project_dir):
    """Create merged PROJECT_GUIDE.md"""
    impl_guide = project_dir / 'Implementation_Guide.md'
    beginner_guide = project_dir / 'BEGINNER_GUIDE.md'
    project_guide = project_dir / 'PROJECT_GUIDE.md'
    
    # Skip if already exists
    if project_guide.exists():
        print(f"  ⏭️  {project_guide.name} already exists, skipping")
        return
    
    impl_content = ''
    beginner_content = ''
    
    if impl_guide.exists():
        with open(impl_guide, 'r', encoding='utf-8') as f:
            impl_content = f.read()
    
    if beginner_guide.exists():
        with open(beginner_guide, 'r', encoding='utf-8') as f:
            beginner_content = f.read()
    
    if not impl_content and not beginner_content:
        print(f"  ⚠️  No guides found in {project_dir}")
        return
    
    # Extract sections
    impl_sections = extract_sections(impl_content, 'implementation') if impl_content else {}
    beginner_sections = extract_sections(beginner_content, 'beginner') if beginner_content else {}
    
    # Create merged guide
    merged = []
    
    # Title
    project_name = project_dir.name.replace('_', ' ').title()
    merged.append(f"# Complete Project Guide: {project_name}")
    merged.append("## دليل المشروع الكامل")
    merged.append("")
    merged.append("---")
    merged.append("")
    
    # Real-world application (from beginner guide)
    if beginner_sections.get('real_world'):
        merged.append(beginner_sections['real_world'])
        merged.append("")
        merged.append("---")
        merged.append("")
    
    # Quick Start section
    merged.append("## 🚀 Quick Start (For Experienced Students)")
    merged.append("## البدء السريع (للطلاب ذوي الخبرة)")
    merged.append("")
    merged.append("> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.")
    merged.append("")
    
    if impl_sections.get('quick_start'):
        # Extract key parts from implementation guide
        merged.append(impl_sections['quick_start'])
    else:
        merged.append("See Complete Tutorial section below for detailed instructions.")
    
    merged.append("")
    merged.append("---")
    merged.append("")
    
    # Complete Tutorial section
    merged.append("## 📚 Complete Tutorial (For Beginners)")
    merged.append("## دليل كامل للمبتدئين")
    merged.append("")
    merged.append("> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.")
    merged.append("")
    
    if beginner_sections.get('tutorial'):
        merged.append(beginner_sections['tutorial'])
    else:
        merged.append("See Implementation Guide for technical details.")
    
    merged.append("")
    merged.append("---")
    merged.append("")
    
    # Course connections
    if beginner_sections.get('course_connections') or 'Course Connection' in beginner_content:
        merged.append("## 🔗 Course Content Connections")
        merged.append("## روابط محتوى الدورة")
        merged.append("")
        merged.append("Each step in this project connects to specific course notebooks. See the tutorial section above for detailed connections.")
        merged.append("")
        merged.append("---")
        merged.append("")
    
    # Troubleshooting
    if beginner_sections.get('troubleshooting'):
        merged.append(beginner_sections['troubleshooting'])
        merged.append("")
        merged.append("---")
        merged.append("")
    
    # Write merged guide
    with open(project_guide, 'w', encoding='utf-8') as f:
        f.write('\n'.join(merged))
    
    print(f"  ✅ Created {project_guide.name}")

def main():
    root = Path('.')
    project_dirs = [d for d in root.rglob('*/PROJECTS/*') if d.is_dir() and 'Template' not in str(d)]
    
    print(f"Found {len(project_dirs)} project directories")
    print("Creating merged PROJECT_GUIDE.md files...\n")
    
    for project_dir in sorted(project_dirs):
        print(f"Processing: {project_dir.relative_to(root)}")
        create_merged_guide(project_dir)
    
    print(f"\n✅ Done!")

if __name__ == '__main__':
    main()

