"""
Unit 1 - Example 1: Introduction to Artificial Intelligence
الوحدة 1 - مثال 1: مقدمة في الذكاء الاصطناعي

This example demonstrates:
1. Basic AI concepts and definitions
2. Types of AI systems
3. Real-world AI applications
4. Simple AI decision-making example
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
        "examples": ["Siri", "Google Translate", "Image Recognition"],
        "arabic": "ذكاء اصطناعي ضيق (ضعيف) - مصمم لمهام محددة"
    },
    "General AI (Strong AI)": {
        "description": "AI with human-level intelligence across all domains",
        "examples": ["Not yet achieved", "Theoretical"],
        "arabic": "ذكاء اصطناعي عام (قوي) - ذكاء على مستوى البشر"
    },
    "Superintelligent AI": {
        "description": "AI that surpasses human intelligence",
        "examples": ["Future concept", "Theoretical"],
        "arabic": "ذكاء اصطناعي فائق - يتجاوز الذكاء البشري"
    }
}

for ai_type, info in ai_types.items():
    print(f"\n{ai_type}:")
    print(f"  {info['arabic']}")
    print(f"  Description: {info['description']}")
    print(f"  Examples: {', '.join(info['examples'])}")

# 3. Simple AI Decision-Making Example
# مثال بسيط على اتخاذ القرار بالذكاء الاصطناعي
print("\n" + "=" * 60)
print("3. Simple AI Decision-Making Example")
print("مثال بسيط على اتخاذ القرار بالذكاء الاصطناعي")
print("=" * 60)

def simple_ai_decision(temperature, humidity, time_of_day):
    """
    Simple rule-based AI system for weather-based activity recommendation.
    نظام ذكاء اصطناعي بسيط قائم على القواعد لتوصية نشاط بناءً على الطقس.
    
    Args:
        temperature: Temperature in Celsius
        humidity: Humidity percentage (0-100)
        time_of_day: 'morning', 'afternoon', or 'evening'
    
    Returns:
        Recommended activity
    """
    # Decision rules / قواعد القرار
    if temperature > 25 and humidity < 60:
        if time_of_day == 'morning':
            return "Go for a jog in the park | اذهب للجري في الحديقة"
        elif time_of_day == 'afternoon':
            return "Go swimming | اذهب للسباحة"
        else:
            return "Take an evening walk | اذهب لنزهة مسائية"
    
    elif temperature < 15:
        return "Stay indoors, read a book | ابق في الداخل واقرأ كتاباً"
    
    elif humidity > 80:
        return "Stay indoors, watch a movie | ابق في الداخل وشاهد فيلماً"
    
    else:
        return "Moderate weather, any outdoor activity is fine | طقس معتدل، أي نشاط خارجي مناسب"

# Test the AI system
# اختبار نظام الذكاء الاصطناعي
print("\nTesting AI Decision System:")
print("اختبار نظام اتخاذ القرار:")

test_cases = [
    (28, 50, 'morning'),
    (30, 45, 'afternoon'),
    (12, 70, 'evening'),
    (20, 85, 'afternoon')
]

for temp, hum, time in test_cases:
    decision = simple_ai_decision(temp, hum, time)
    print(f"\nTemperature: {temp}°C, Humidity: {hum}%, Time: {time}")
    print(f"Recommendation: {decision}")

# 4. AI Applications in Real World
# تطبيقات الذكاء الاصطناعي في العالم الحقيقي
print("\n" + "=" * 60)
print("4. AI Applications in Real World")
print("تطبيقات الذكاء الاصطناعي في العالم الحقيقي")
print("=" * 60)

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
    ]
}

for domain, apps in applications.items():
    print(f"\n{domain}:")
    for app in apps:
        print(f"  - {app}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
