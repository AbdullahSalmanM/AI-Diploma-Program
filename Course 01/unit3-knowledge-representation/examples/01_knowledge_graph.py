"""
Unit 3 - Example 1: Knowledge Graph Representation
الوحدة 3 - مثال 1: تمثيل الرسم البياني للمعرفة

This example demonstrates:
1. Creating a knowledge graph
2. Representing relationships
3. Querying the knowledge graph
4. Visualizing knowledge structure
"""

print("=" * 60)
print("Example 1: Knowledge Graph Representation")
print("مثال 1: تمثيل الرسم البياني للمعرفة")
print("=" * 60)

# Knowledge Graph: Family Relationships
# الرسم البياني للمعرفة: علاقات العائلة
knowledge_graph = {
    'Ahmed': {
        'is_parent_of': ['Sara', 'Omar'],
        'is_married_to': ['Fatima'],
        'age': 45,
        'profession': 'Engineer'
    },
    'Fatima': {
        'is_parent_of': ['Sara', 'Omar'],
        'is_married_to': ['Ahmed'],
        'age': 42,
        'profession': 'Doctor'
    },
    'Sara': {
        'is_child_of': ['Ahmed', 'Fatima'],
        'is_sibling_of': ['Omar'],
        'age': 18,
        'profession': 'Student'
    },
    'Omar': {
        'is_child_of': ['Ahmed', 'Fatima'],
        'is_sibling_of': ['Sara'],
        'age': 15,
        'profession': 'Student'
    }
}

def query_knowledge_graph(graph, person, relationship):
    """
    Query the knowledge graph for relationships.
    استعلام الرسم البياني للمعرفة عن العلاقات.
    
    Args:
        graph: Knowledge graph dictionary
        person: Person to query about
        relationship: Type of relationship to find
    
    Returns:
        List of related people
    """
    if person not in graph:
        return []
    
    return graph[person].get(relationship, [])

def find_all_relationships(graph, person):
    """
    Find all relationships for a person.
    العثور على جميع العلاقات لشخص ما.
    """
    if person not in graph:
        return {}
    
    return graph[person]

# Example queries
print("\n1. Querying Knowledge Graph")
print("استعلام الرسم البياني للمعرفة")
print("-" * 60)

# Who are Ahmed's children?
print("\nWho are Ahmed's children? / من هم أطفال أحمد؟")
children = query_knowledge_graph(knowledge_graph, 'Ahmed', 'is_parent_of')
print(f"  Answer: {children}")

# Who is Sara's sibling?
print("\nWho is Sara's sibling? / من هو شقيق سارة؟")
siblings = query_knowledge_graph(knowledge_graph, 'Sara', 'is_sibling_of')
print(f"  Answer: {siblings}")

# All relationships for Fatima
print("\nAll relationships for Fatima / جميع علاقات فاطمة:")
relationships = find_all_relationships(knowledge_graph, 'Fatima')
for rel_type, rel_value in relationships.items():
    print(f"  {rel_type}: {rel_value}")

# Rule-Based System Example
print("\n" + "=" * 60)
print("2. Rule-Based System")
print("نظام قائم على القواعد")
print("=" * 60)

# Rules for determining if someone can drive
# قواعد لتحديد ما إذا كان شخص ما يمكنه القيادة
def can_drive(person, graph):
    """
    Rule-based system: Can person drive?
    نظام قائم على القواعد: هل يمكن للشخص القيادة؟
    """
    if person not in graph:
        return False, "Person not found"
    
    age = graph[person].get('age', 0)
    profession = graph[person].get('profession', '')
    
    # Rule 1: Must be 18 or older
    if age < 18:
        return False, "Too young to drive (must be 18+)"
    
    # Rule 2: Must not be a student (simplified rule)
    if profession == 'Student':
        return False, "Students need special permit"
    
    # Rule 3: If 18+ and not student, can drive
    return True, "Can drive"

# Test rules
print("\nTesting driving rules:")
for person in knowledge_graph.keys():
    can_drive_result, reason = can_drive(person, knowledge_graph)
    status = "✓ Can drive" if can_drive_result else "✗ Cannot drive"
    print(f"\n{person} (age {knowledge_graph[person]['age']}):")
    print(f"  {status} - {reason}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
