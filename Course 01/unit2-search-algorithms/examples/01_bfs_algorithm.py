"""
Unit 2 - Example 1: Breadth-First Search (BFS)
الوحدة 2 - مثال 1: البحث بالعرض أولاً

This example demonstrates:
1. BFS algorithm implementation
2. Graph representation
3. Finding shortest path
"""

from collections import deque

print("=" * 60)
print("Example 1: Breadth-First Search (BFS)")
print("مثال 1: البحث بالعرض أولاً")
print("=" * 60)

# Graph representation using adjacency list
# تمثيل الرسم البياني باستخدام قائمة الجوار
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
    # Initialize queue with starting node
    # تهيئة قائمة الانتظار بالعقدة البداية
    queue = deque([(start, [start])])
    visited = set([start])
    
    print(f"\nSearching from {start} to {goal}...")
    print(f"البحث من {start} إلى {goal}...")
    
    while queue:
        # Get next node from queue
        # الحصول على العقدة التالية من قائمة الانتظار
        current, path = queue.popleft()
        
        print(f"  Visiting: {current}, Path: {' -> '.join(path)}")
        print(f"  زيارة: {current}, المسار: {' -> '.join(path)}")
        
        # Check if goal reached
        # التحقق من الوصول للهدف
        if current == goal:
            print(f"\n✓ Goal reached! Path: {' -> '.join(path)}")
            print(f"✓ تم الوصول للهدف! المسار: {' -> '.join(path)}")
            return path
        
        # Explore neighbors
        # استكشاف الجيران
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    print(f"\n✗ Goal not reachable from {start}")
    print(f"✗ الهدف غير قابل للوصول من {start}")
    return None

# Example usage
# مثال على الاستخدام
print("\nGraph structure:")
print("هيكل الرسم البياني:")
for node, neighbors in graph.items():
    print(f"  {node}: {neighbors}")

print("\n" + "-" * 60)
result = bfs(graph, 'A', 'F')

if result:
    print(f"\nShortest path length: {len(result) - 1}")
    print(f"طول أقصر مسار: {len(result) - 1}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

