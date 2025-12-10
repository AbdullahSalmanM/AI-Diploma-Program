"""
Unit 2 - Example 2: Depth-First Search (DFS)
الوحدة 2 - مثال 2: البحث بالعمق أولاً

This example demonstrates:
1. DFS algorithm implementation
2. Recursive and iterative approaches
3. Finding paths in graphs
"""

print("=" * 60)
print("Example 2: Depth-First Search (DFS)")
print("مثال 2: البحث بالعمق أولاً")
print("=" * 60)

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs_recursive(graph, node, goal, visited=None, path=None):
    """
    Recursive DFS implementation.
    تنفيذ DFS العودي.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(node)
    path = path + [node]
    
    if node == goal:
        return path
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, goal, visited, path)
            if result:
                return result
    
    return None

def dfs_iterative(graph, start, goal):
    """
    Iterative DFS implementation using stack.
    تنفيذ DFS التكراري باستخدام المكدس.
    """
    stack = [(start, [start])]
    visited = set([start])
    
    print(f"\nSearching for path from {start} to {goal}...")
    print(f"البحث عن مسار من {start} إلى {goal}...")
    
    while stack:
        current, path = stack.pop()
        
        print(f"  Visiting: {current}, Path: {' -> '.join(path)}")
        
        if current == goal:
            print(f"\n✓ Goal found! Path: {' -> '.join(path)}")
            return path
        
        # Add neighbors to stack (reverse order for consistent behavior)
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    
    print(f"\n✗ No path found from {start} to {goal}")
    return None

# Test DFS
print("\n" + "=" * 60)
print("Testing DFS Algorithm (Iterative)")
print("اختبار خوارزمية DFS (تكراري)")
print("=" * 60)

path1 = dfs_iterative(graph, 'A', 'F')
print(f"\nResult: {path1}")

print("\n" + "-" * 60)
print("Testing DFS Algorithm (Recursive)")
print("اختبار خوارزمية DFS (عودي)")
print("-" * 60)

path2 = dfs_recursive(graph, 'D', 'C')
print(f"\nResult: {path2}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
