"""
Unit 3 - Example 1: Knowledge Graph Representation
الوحدة 3 - مثال 1: تمثيل الرسم البياني للمعرفة

This example demonstrates knowledge representation using graphs.
"""

class KnowledgeGraph:
    """Simple knowledge graph implementation."""
    
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_fact(self, subject, relation, object):
        """Add a fact to the knowledge graph."""
        if subject not in self.nodes:
            self.nodes[subject] = []
        self.nodes[subject].append((relation, object))
        self.edges.append((subject, relation, object))
    
    def query(self, subject, relation=None):
        """Query the knowledge graph."""
        if subject not in self.nodes:
            return []
        
        results = self.nodes[subject]
        if relation:
            results = [obj for rel, obj in results if rel == relation]
        return results

# Example usage
kg = KnowledgeGraph()

# Add facts
kg.add_fact("Socrates", "is_a", "philosopher")
kg.add_fact("Socrates", "lived_in", "Athens")
kg.add_fact("Plato", "is_a", "philosopher")
kg.add_fact("Plato", "student_of", "Socrates")

print("Knowledge Graph:")
print(kg.query("Socrates"))
print(kg.query("Socrates", "is_a"))

