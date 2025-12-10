"""
Unit 1 - Example 1: Introduction to Artificial Intelligence
الوحدة 1 - مثال 1: مقدمة في الذكاء الاصطناعي

This example demonstrates:
1. Basic AI concepts
2. Types of AI systems
3. Real-world AI applications
"""

print("=" * 60)
print("Example 1: Introduction to Artificial Intelligence")
print("مثال 1: مقدمة في الذكاء الاصطناعي")
print("=" * 60)

# 1. What is AI?
# ما هو الذكاء الاصطناعي؟
print("\n1. What is Artificial Intelligence?")
print("ما هو الذكاء الاصطناعي؟")
print("-" * 60)

ai_definition = """
Artificial Intelligence (AI) is the simulation of human intelligence 
in machines that are programmed to think and learn like humans.

الذكاء الاصطناعي هو محاكاة الذكاء البشري في الآلات المبرمجة 
للتفكير والتعلم مثل البشر.
"""

print(ai_definition)

# 2. Types of AI Systems
# أنواع أنظمة الذكاء الاصطناعي
print("\n2. Types of AI Systems")
print("أنواع أنظمة الذكاء الاصطناعي")
print("-" * 60)

ai_types = {
    "Narrow AI (Weak AI)": {
        "description": "AI designed for specific tasks",
        "examples": ["Voice assistants (Siri, Alexa)", "Image recognition", "Chess-playing programs"],
        "arabic": "ذكاء اصطناعي ضيق (ضعيف)"
    },
    "General AI (Strong AI)": {
        "description": "AI with human-level intelligence across all tasks",
        "examples": ["Not yet achieved", "Theoretical concept"],
        "arabic": "ذكاء اصطناعي عام (قوي)"
    },
    "Superintelligence": {
        "description": "AI that surpasses human intelligence",
        "examples": ["Future possibility", "Subject of research"],
        "arabic": "الذكاء الفائق"
    }
}

for ai_type, info in ai_types.items():
    print(f"\n{ai_type} ({info['arabic']}):")
    print(f"  Description: {info['description']}")
    print(f"  Examples: {', '.join(info['examples'])}")

# 3. AI Applications in Real World
# تطبيقات الذكاء الاصطناعي في العالم الحقيقي
print("\n3. AI Applications in Real World")
print("تطبيقات الذكاء الاصطناعي في العالم الحقيقي")
print("-" * 60)

applications = {
    "Healthcare": [
        "Medical image analysis",
        "Drug discovery",
        "Personalized treatment plans"
    ],
    "Transportation": [
        "Autonomous vehicles",
        "Traffic optimization",
        "Route planning"
    ],
    "Finance": [
        "Fraud detection",
        "Algorithmic trading",
        "Credit scoring"
    ],
    "Education": [
        "Personalized learning",
        "Automated grading",
        "Intelligent tutoring systems"
    ],
    "Entertainment": [
        "Recommendation systems",
        "Game AI",
        "Content generation"
    ]
}

for domain, examples in applications.items():
    print(f"\n{domain}:")
    for example in examples:
        print(f"  - {example}")

# 4. AI vs Machine Learning vs Deep Learning
# الذكاء الاصطناعي مقابل تعلم الآلة مقابل التعلم العميق
print("\n4. AI vs Machine Learning vs Deep Learning")
print("الذكاء الاصطناعي مقابل تعلم الآلة مقابل التعلم العميق")
print("-" * 60)

relationship = """
AI (Artificial Intelligence)
  └── Machine Learning (subset of AI)
      └── Deep Learning (subset of Machine Learning)

الذكاء الاصطناعي
  └── تعلم الآلة (جزء من الذكاء الاصطناعي)
      └── التعلم العميق (جزء من تعلم الآلة)
"""

print(relationship)

comparison = {
    "AI": {
        "scope": "Broadest - any technique enabling machines to mimic human intelligence",
        "example": "Expert systems, rule-based systems"
    },
    "Machine Learning": {
        "scope": "Subset of AI - systems that learn from data",
        "example": "Classification, regression, clustering"
    },
    "Deep Learning": {
        "scope": "Subset of ML - uses neural networks with multiple layers",
        "example": "Image recognition, natural language processing"
    }
}

for concept, info in comparison.items():
    print(f"\n{concept}:")
    print(f"  Scope: {info['scope']}")
    print(f"  Example: {info['example']}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

