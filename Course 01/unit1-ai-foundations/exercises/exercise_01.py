"""
Unit 1 - Exercise 1: AI Fundamentals
الوحدة 1 - تمرين 1: أساسيات الذكاء الاصطناعي

Complete the following exercises to practice AI fundamentals.
أكمل التمارين التالية لممارسة أساسيات الذكاء الاصطناعي.
"""

# Exercise 1: Define AI
# التمرين 1: تعريف الذكاء الاصطناعي
print("Exercise 1: Define AI")
print("التمرين 1: تعريف الذكاء الاصطناعي")
print("-" * 60)

# TODO: Write your own definition of AI in 2-3 sentences
# TODO: اكتب تعريفك الخاص للذكاء الاصطناعي في 2-3 جمل
ai_definition = """
Your definition here / تعريفك هنا:
"""

print(ai_definition)

# Exercise 2: Identify AI Types
# التمرين 2: تحديد أنواع الذكاء الاصطناعي
print("\nExercise 2: Identify AI Types")
print("التمرين 2: تحديد أنواع الذكاء الاصطناعي")
print("-" * 60)

# TODO: Classify each system as Narrow AI, General AI, or Superintelligent AI
# TODO: صنف كل نظام كذكاء اصطناعي ضيق، عام، أو فائق
systems = [
    "Siri voice assistant",
    "Self-driving car",
    "Chess-playing computer",
    "Human-like robot that can do any task",
    "AI that is smarter than all humans combined"
]

# TODO: Create a dictionary mapping each system to its AI type
# TODO: أنشئ قاموس يربط كل نظام بنوع الذكاء الاصطناعي
system_types = {}

for system in systems:
    # TODO: Classify the system
    # system_types[system] = "Your classification here"
    pass

# Exercise 3: AI Application Research
# التمرين 3: بحث عن تطبيقات الذكاء الاصطناعي
print("\nExercise 3: AI Application Research")
print("التمرين 3: بحث عن تطبيقات الذكاء الاصطناعي")
print("-" * 60)

# TODO: Research and list 3 AI applications in a field of your choice
# TODO: ابحث واذكر 3 تطبيقات للذكاء الاصطناعي في مجال من اختيارك
chosen_field = "Your field here / المجال الذي اخترته:"
applications = [
    "Application 1 / التطبيق 1:",
    "Application 2 / التطبيق 2:",
    "Application 3 / التطبيق 3:"
]

print(f"\nField: {chosen_field}")
for app in applications:
    print(f"  - {app}")

# Exercise 4: Simple Rule-Based System
# التمرين 4: نظام بسيط قائم على القواعد
print("\nExercise 4: Simple Rule-Based System")
print("التمرين 4: نظام بسيط قائم على القواعد")
print("-" * 60)

def recommend_movie(age, genre_preference, mood):
    """
    TODO: Create a rule-based system that recommends a movie
    based on age, genre preference, and mood.
    
    TODO: أنشئ نظاماً قائماً على القواعد يوصي بفيلم
    بناءً على العمر، تفضيل النوع، والمزاج.
    
    Args:
        age: Person's age
        genre_preference: 'action', 'comedy', 'drama', 'horror'
        mood: 'happy', 'sad', 'excited', 'relaxed'
    
    Returns:
        Movie recommendation
    """
    # TODO: Implement your recommendation logic
    # TODO: نفذ منطق التوصية الخاص بك
    pass

# Test your function
# اختبر دالتك
print("\nTesting movie recommendation system:")
test_cases = [
    (25, 'action', 'excited'),
    (15, 'comedy', 'happy'),
    (30, 'drama', 'sad')
]

for age, genre, mood in test_cases:
    recommendation = recommend_movie(age, genre, mood)
    print(f"Age: {age}, Genre: {genre}, Mood: {mood}")
    print(f"Recommendation: {recommendation}")

print("\n" + "=" * 60)
print("Exercises completed! Check solutions/ folder for answers.")
print("تم إكمال التمارين! راجع مجلد solutions/ للإجابات.")
print("=" * 60)
