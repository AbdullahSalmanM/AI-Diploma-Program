"""
Unit 2 - Exercise 1: Search Algorithms
الوحدة 2 - تمرين 1: خوارزميات البحث

Complete the following exercises to practice search algorithms.
أكمل التمارين التالية لممارسة خوارزميات البحث.
"""

from collections import deque

# Exercise 1: Complete BFS Implementation
# التمرين 1: أكمل تنفيذ BFS
print("Exercise 1: Complete BFS")
print("التمرين 1: أكمل BFS")
print("-" * 60)

graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2'],
    '5': ['2', '6'],
    '6': ['3', '5']
}

def bfs_complete(graph, start, goal):
    """
    TODO: Complete the BFS implementation.
    TODO: أكمل تنفيذ BFS.
    
    Args:
        graph: Dictionary representing the graph
        start: Starting node
        goal: Target node
    
    Returns:
        Shortest path from start to goal
    """
    # TODO: Initialize queue with start node
    # TODO: Initialize visited set
    # TODO: Implement BFS algorithm
    # TODO: Return path when goal is found
    pass

# Test your implementation
print("\nTesting BFS:")
result = bfs_complete(graph, '1', '6')
print(f"Path from 1 to 6: {result}")

# Exercise 2: DFS Path Finding
# التمرين 2: إيجاد المسار باستخدام DFS
print("\n" + "=" * 60)
print("Exercise 2: DFS Path Finding")
print("التمرين 2: إيجاد المسار باستخدام DFS")
print("=" * 60)

def dfs_path(graph, start, goal):
    """
    TODO: Implement DFS to find any path from start to goal.
    TODO: نفذ DFS لإيجاد أي مسار من البداية إلى الهدف.
    """
    # TODO: Implement DFS (recursive or iterative)
    pass

# Test your implementation
result = dfs_path(graph, '4', '3')
print(f"Path from 4 to 3: {result}")

# Exercise 3: Maze Solver
# التمرين 3: حل المتاهة
print("\n" + "=" * 60)
print("Exercise 3: Maze Solver")
print("التمرين 3: حل المتاهة")
print("=" * 60)

# Simple maze representation (0 = wall, 1 = path)
# تمثيل متاهة بسيطة (0 = جدار، 1 = مسار)
maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1]
]

def solve_maze(maze, start, end):
    """
    TODO: Use BFS or DFS to solve the maze.
    TODO: استخدم BFS أو DFS لحل المتاهة.
    
    Args:
        maze: 2D list representing the maze
        start: (row, col) starting position
        end: (row, col) ending position
    
    Returns:
        List of (row, col) positions forming the path
    """
    # TODO: Implement maze solving algorithm
    pass

# Test maze solver
start_pos = (0, 0)
end_pos = (3, 3)
path = solve_maze(maze, start_pos, end_pos)
print(f"Path from {start_pos} to {end_pos}: {path}")

print("\n" + "=" * 60)
print("Exercises completed! Check solutions/ folder for answers.")
print("تم إكمال التمارين! راجع مجلد solutions/ للإجابات.")
print("=" * 60)

