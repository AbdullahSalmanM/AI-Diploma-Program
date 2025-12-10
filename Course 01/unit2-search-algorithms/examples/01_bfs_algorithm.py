"""
Unit 2 - Example 1: Breadth-First Search (BFS)
الوحدة 2 - مثال 1: البحث بالعرض أولاً

This example demonstrates:
1. BFS algorithm implementation
2. Finding shortest path in a graph
3. Visualizing the search process
"""

from collections import deque

print("=" * 60)
print("Example 1: Breadth-First Search (BFS)")
print("مثال 1: البحث بالعرض أولاً")
print("=" * 60)

# Graph representation
# تمثيل الرسم البياني
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start, goal):
    """
    Breadth-First Search algorithm.
    خوارزمية البحث بالعرض أولاً.
    
    Args:
        graph: Dictionary representing the graph
        start: Starting node
        goal: Target node
    
    Returns:
        Path from start to goal, or None if not found
    """
    # Queue for BFS
    queue = deque([(start, [start])])
    visited = set([start])
    
    print(f"\nSearching for path from {start} to {goal}...")
    print(f"البحث عن مسار من {start} إلى {goal}...")
    
    while queue:
        current, path = queue.popleft()
        
        print(f"  Visiting: {current}, Path: {' -> '.join(path)}")
        
        if current == goal:
            print(f"\n✓ Goal found! Path: {' -> '.join(path)}")
            return path
        
        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    print(f"\n✗ No path found from {start} to {goal}")
    return None

# Test BFS
print("\n" + "=" * 60)
print("Testing BFS Algorithm")
print("اختبار خوارزمية BFS")
print("=" * 60)

# Test case 1
path1 = bfs(graph, 'A', 'F')
print(f"\nResult: {path1}")

# Test case 2
print("\n" + "-" * 60)
path2 = bfs(graph, 'D', 'C')
print(f"\nResult: {path2}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
