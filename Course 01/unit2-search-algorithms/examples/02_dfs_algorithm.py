"""
Unit 2 - Example 2: Depth-First Search (DFS)
الوحدة 2 - مثال 2: البحث بالعمق أولاً

This example demonstrates DFS algorithm implementation.
"""

def dfs(graph, start, goal, visited=None, path=None):
    """
    Depth-First Search algorithm (recursive).
    خوارزمية البحث بالعمق أولاً (تعاودية).
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path = path + [start]
    
    print(f"  Visiting: {start}, Path: {' -> '.join(path)}")
    
    if start == goal:
        return path
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result
    
    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS from A to F:")
result = dfs(graph, 'A', 'F')
if result:
    print(f"Path found: {' -> '.join(result)}")

