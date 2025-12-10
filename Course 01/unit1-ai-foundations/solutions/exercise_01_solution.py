"""
Unit 1 - Exercise 1: Solution
الوحدة 1 - تمرين 1: الحل

Complete solutions to Exercise 1.
"""

print("=" * 60)
print("Exercise 1: Solutions")
print("تمرين 1: الحلول")
print("=" * 60)

# Solution 1: AI Definition
print("\nSolution 1: AI Definition")
print("-" * 60)

ai_definition = """
Artificial Intelligence (AI) is a branch of computer science that aims 
to create systems capable of performing tasks that typically require 
human intelligence, such as learning, reasoning, and problem-solving.

الذكاء الاصطناعي هو فرع من علوم الحاسوب يهدف إلى إنشاء أنظمة قادرة 
على أداء مهام تتطلب عادة ذكاء بشرياً، مثل التعلم والاستدلال وحل المشاكل.
"""

print(ai_definition)

# Solution 2: AI Types Classification
print("\nSolution 2: AI Types Classification")
print("-" * 60)

applications = {
    "Email spam filter": "Narrow AI",
    "Self-driving car": "Narrow AI",
    "Calculator": "Not AI",
    "ChatGPT": "Narrow AI",
    "Human brain": "Not AI",
    "Facial recognition system": "Narrow AI"
}

print("\nClassifications:")
for app, classification in applications.items():
    print(f"  {app}: {classification}")

# Solution 3: Real-World Applications (Example: Healthcare)
print("\nSolution 3: Real-World Applications (Example: Healthcare)")
print("-" * 60)

my_field = "Healthcare"
applications_in_my_field = [
    "Medical image analysis for disease detection",
    "Drug discovery and development",
    "Personalized treatment recommendations"
]

print(f"\nAI applications in {my_field}:")
for i, app in enumerate(applications_in_my_field, 1):
    print(f"  {i}. {app}")

# Solution 4: AI vs ML vs DL Classification
print("\nSolution 4: AI vs ML vs DL Classification")
print("-" * 60)

techniques = {
    "Rule-based expert system": "AI",
    "Linear regression": "ML",
    "Convolutional Neural Network": "DL",
    "Decision tree": "ML",
    "Recurrent Neural Network": "DL",
    "If-else statements": "Not AI/ML/DL"
}

print("\nClassifications:")
for technique, classification in techniques.items():
    print(f"  {technique}: {classification}")

print("\n" + "=" * 60)
print("Solutions completed!")
print("تم إكمال الحلول!")
print("=" * 60)

