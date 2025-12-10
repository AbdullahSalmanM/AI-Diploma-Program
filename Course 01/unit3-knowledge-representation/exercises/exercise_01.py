"""
Unit 3 - Exercise 1: Knowledge Representation
الوحدة 3 - تمرين 1: تمثيل المعرفة

Complete the following exercises.
أكمل التمارين التالية.
"""

# Exercise 1: Create Knowledge Graph
# التمرين 1: إنشاء رسم بياني للمعرفة
print("Exercise 1: Create Knowledge Graph")
print("التمرين 1: إنشاء رسم بياني للمعرفة")
print("-" * 60)

# TODO: Create a knowledge graph for a domain of your choice
# (e.g., animals, vehicles, food)
# TODO: أنشئ رسم بياني للمعرفة لمجال من اختيارك

knowledge_graph = {
    # TODO: Add nodes and relationships
    # TODO: أضف العقد والعلاقات
}

# Exercise 2: Rule-Based System
# التمرين 2: نظام قائم على القواعد
print("\n" + "=" * 60)
print("Exercise 2: Rule-Based System")
print("التمرين 2: نظام قائم على القواعد")
print("=" * 60)

def recommend_activity(weather, temperature, time_of_day):
    """
    TODO: Create a rule-based system that recommends an activity
    based on weather, temperature, and time of day.
    
    TODO: أنشئ نظاماً قائماً على القواعد يوصي بنشاط
    بناءً على الطقس ودرجة الحرارة ووقت اليوم.
    """
    # TODO: Implement rules
    # TODO: نفذ القواعد
    pass

# Test your system
test_cases = [
    ('sunny', 25, 'morning'),
    ('rainy', 15, 'afternoon'),
    ('cloudy', 20, 'evening')
]

for weather, temp, time in test_cases:
    recommendation = recommend_activity(weather, temp, time)
    print(f"Weather: {weather}, Temp: {temp}°C, Time: {time}")
    print(f"Recommendation: {recommendation}\n")

print("=" * 60)
print("Exercises completed! Check solutions/ folder.")
print("تم إكمال التمارين! راجع مجلد solutions/.")
print("=" * 60)

