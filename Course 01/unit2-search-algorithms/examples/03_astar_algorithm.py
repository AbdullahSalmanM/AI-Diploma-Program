"""
Unit 2 - Example 3: A* Algorithm
الوحدة 2 - مثال 3: خوارزمية A*

This example demonstrates:
1. A* algorithm implementation
2. Heuristic functions
3. Optimal pathfinding
"""

import heapq

print("=" * 60)
print("Example 3: A* Algorithm")
print("مثال 3: خوارزمية A*")
print("=" * 60)

# Graph with coordinates for heuristic calculation
# الرسم البياني مع الإحداثيات لحساب الدالة الاستدلالية
graph = {
    'A': {'neighbors': ['B', 'C'], 'coords': (0, 0)},
    'B': {'neighbors': ['A', 'D', 'E'], 'coords': (1, 1)},
    'C': {'neighbors': ['A', 'F'], 'coords': (2, 0)},
    'D': {'neighbors': ['B'], 'coords': (1, 2)},
    'E': {'neighbors': ['B', 'F'], 'coords': (2, 2)},
    'F': {'neighbors': ['C', 'E'], 'coords': (3, 1)}
}

def heuristic(node1, node2):
    """
    Manhattan distance heuristic.
    دالة استدلالية بمسافة مانهاتن.
    """
    x1, y1 = graph[node1]['coords']
    x2, y2 = graph[node2]['coords']
    return abs(x1 - x2) + abs(y1 - y2)

def astar(graph, start, goal):
    """
    A* pathfinding algorithm.
    خوارزمية البحث عن المسار A*.
    """
    # Priority queue: (f_score, g_score, node, path)
    open_set = [(0, 0, start, [start])]
    visited = set()
    
    print(f"\nSearching for optimal path from {start} to {goal}...")
    print(f"البحث عن المسار الأمثل من {start} إلى {goal}...")
    
    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        print(f"  Visiting: {current}, Path: {' -> '.join(path)}, Cost: {g_score}")
        
        if current == goal:
            print(f"\n✓ Optimal path found! Path: {' -> '.join(path)}, Total cost: {g_score}")
            return path
        
        # Explore neighbors
        for neighbor in graph[current]['neighbors']:
            if neighbor in visited:
                continue
            
            # Calculate costs
            new_g_score = g_score + 1  # Assuming edge cost of 1
            h_score = heuristic(neighbor, goal)
            f_score = new_g_score + h_score
            
            heapq.heappush(open_set, (f_score, new_g_score, neighbor, path + [neighbor]))
    
    print(f"\n✗ No path found from {start} to {goal}")
    return None

# Test A*
print("\n" + "=" * 60)
print("Testing A* Algorithm")
print("اختبار خوارزمية A*")
print("=" * 60)

path = astar(graph, 'A', 'F')
print(f"\nFinal Result: {path}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
