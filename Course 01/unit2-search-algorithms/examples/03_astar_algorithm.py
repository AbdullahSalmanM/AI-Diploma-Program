"""
Unit 2 - Example 3: A* Search Algorithm
الوحدة 2 - مثال 3: خوارزمية البحث A*

This example demonstrates A* algorithm with heuristic function.
"""

import heapq

def heuristic(node, goal):
    """Simple heuristic function (Manhattan distance example)"""
    # In a grid, this would be |x1-x2| + |y1-y2|
    # For this example, using simple distance
    return abs(ord(node) - ord(goal))

def astar(graph, start, goal):
    """
    A* Search Algorithm.
    خوارزمية البحث A*.
    """
    open_set = [(0, start, [start])]  # (f_score, node, path)
    closed_set = set()
    
    while open_set:
        f, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in closed_set:
                g = len(path)  # Cost from start
                h = heuristic(neighbor, goal)  # Heuristic
                f_new = g + h
                heapq.heappush(open_set, (f_new, neighbor, path + [neighbor]))
    
    return None

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("A* from A to F:")
result = astar(graph, 'A', 'F')
if result:
    print(f"Optimal path: {' -> '.join(result)}")

