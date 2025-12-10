#!/usr/bin/env python3
"""
Script to create course content structure following Course 02-06 pattern
"""
import os

def create_unit_structure(course_path, unit_name, unit_num):
    """Create complete unit structure"""
    unit_path = os.path.join(course_path, f"unit{unit_num}-{unit_name}")
    
    # Create directories
    dirs = ['examples', 'exercises', 'solutions', 'quizzes', 'tests']
    for d in dirs:
        os.makedirs(os.path.join(unit_path, d), exist_ok=True)
    
    print(f"Created structure for {unit_name}")

# Course 01 units
course01_units = [
    (1, "ai-foundations"),
    (2, "search-algorithms"),
    (3, "knowledge-representation"),
    (4, "neural-networks-basics")
]

course_path = "Course 01"
for num, name in course01_units:
    create_unit_structure(course_path, name, num)

print("Course 01 structure created!")
