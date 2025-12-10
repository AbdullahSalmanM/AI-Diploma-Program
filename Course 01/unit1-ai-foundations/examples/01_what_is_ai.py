"""
Example 01: What is Artificial Intelligence? | ما هو الذكاء الاصطناعي؟
AIAT 111 - Unit 1: AI Foundations

This example introduces the fundamental concepts of Artificial Intelligence.
"""

# ============================================================================
# What is AI? | ما هو الذكاء الاصطناعي؟
# ============================================================================

print("=" * 60)
print("What is Artificial Intelligence? | ما هو الذكاء الاصطناعي؟")
print("=" * 60)

# Definition of AI
ai_definition = """
Artificial Intelligence (AI) is the simulation of human intelligence 
in machines that are programmed to think and learn like humans.

الذكاء الاصطناعي هو محاكاة الذكاء البشري في الآلات المبرمجة 
للتفكير والتعلم مثل البشر.
"""

print(ai_definition)

# Key Characteristics of AI
print("\n" + "=" * 60)
print("Key Characteristics of AI | خصائص الذكاء الاصطناعي الرئيسية")
print("=" * 60)

ai_characteristics = {
    "Learning": "Ability to learn from data and experience",
    "Reasoning": "Ability to solve problems and make decisions",
    "Perception": "Ability to interpret and understand input",
    "Language Understanding": "Ability to understand and generate language",
    "Problem Solving": "Ability to find solutions to complex problems"
}

for characteristic, description in ai_characteristics.items():
    print(f"\n{characteristic}:")
    print(f"  {description}")

# Types of AI
print("\n" + "=" * 60)
print("Types of AI Systems | أنواع أنظمة الذكاء الاصطناعي")
print("=" * 60)

ai_types = {
    "Narrow AI (Weak AI)": {
        "description": "AI designed for specific tasks",
        "examples": ["Siri", "Google Translate", "Image recognition", "Chess-playing AI"]
    },
    "General AI (Strong AI)": {
        "description": "AI with human-level intelligence across all tasks",
        "examples": ["Not yet achieved", "Theoretical concept"]
    },
    "Superintelligence": {
        "description": "AI that surpasses human intelligence",
        "examples": ["Future possibility", "Subject of research"]
    }
}

for ai_type, info in ai_types.items():
    print(f"\n{ai_type}:")
    print(f"  Description: {info['description']}")
    print(f"  Examples: {', '.join(info['examples'])}")

# AI Applications
print("\n" + "=" * 60)
print("AI Applications | تطبيقات الذكاء الاصطناعي")
print("=" * 60)

applications = {
    "Healthcare": ["Medical diagnosis", "Drug discovery", "Personalized treatment"],
    "Transportation": ["Self-driving cars", "Traffic optimization", "Route planning"],
    "Finance": ["Fraud detection", "Algorithmic trading", "Credit scoring"],
    "Education": ["Personalized learning", "Automated grading", "Tutoring systems"],
    "Entertainment": ["Recommendation systems", "Game AI", "Content generation"]
}

for domain, examples in applications.items():
    print(f"\n{domain}:")
    for example in examples:
        print(f"  - {example}")

# AI vs Machine Learning vs Deep Learning
print("\n" + "=" * 60)
print("AI vs Machine Learning vs Deep Learning")
print("الذكاء الاصطناعي مقابل تعلم الآلة مقابل التعلم العميق")
print("=" * 60)

relationship = """
AI (Artificial Intelligence)
  └── ML (Machine Learning) - Subset of AI
        └── DL (Deep Learning) - Subset of ML

AI is the broadest concept
  ↓
ML is a method to achieve AI
  ↓
DL is a technique within ML
"""

print(relationship)

print("\n" + "=" * 60)
print("Example Complete! | اكتمل المثال!")
print("=" * 60)

