# Quiz 02: Search Algorithms | اختبار 2: خوارزميات البحث
## AIAT 111 - Unit 2

**Time Limit:** 45 minutes | **الوقت المحدد:** 45 دقيقة  
**Total Points:** 100 points | **إجمالي النقاط:** 100 نقطة

---

## Part 1: Multiple Choice | الجزء 1: الاختيار من متعدد
**(40 points | 40 نقطة)**

### Question 1 (10 points)
Which data structure does BFS use?

أ) Stack  
ب) Queue  
ج) Priority Queue  
د) Set

**Answer:** ب

---

### Question 2 (10 points)
DFS is optimal for:

أ) Finding shortest path in unweighted graph  
ب) Finding any path  
ج) Finding path with minimum cost  
د) All of the above

**Answer:** ب

---

### Question 3 (10 points)
A* algorithm uses:

أ) Only cost from start (g)  
ب) Only heuristic (h)  
ج) Both g and h (f = g + h)  
د) Neither

**Answer:** ج

---

### Question 4 (10 points)
A heuristic function must be:

أ) Always accurate  
ب) Admissible (never overestimate)  
ج) Always underestimate  
د) Exact

**Answer:** ب

---

## Part 2: Code Writing | الجزء 2: كتابة الكود
**(30 points | 30 نقطة)**

### Question 5 (30 points)
Complete the BFS function:

```python
from collections import deque

def bfs(graph, start, goal):
    # TODO: Implement BFS
    # TODO: اكتب خوارزمية BFS
    pass
```

**Answer Key:**
```python
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

---

## Part 3: Short Answer | الجزء 3: إجابة قصيرة
**(30 points | 30 نقطة)**

### Question 6 (15 points)
Explain when to use BFS vs DFS.

**Answer Key:**
- BFS: When you need the shortest path, or when the solution is likely close to the start
- DFS: When memory is limited, or when you need any solution (not necessarily shortest)

---

### Question 7 (15 points)
What makes A* optimal and complete?

**Answer Key:**
- Optimal: Uses admissible heuristic (never overestimates), ensuring shortest path
- Complete: Will find solution if one exists (given finite graph and admissible heuristic)

---

**For:** AIAT 111 - Introduction to AI Applications and Concepts

