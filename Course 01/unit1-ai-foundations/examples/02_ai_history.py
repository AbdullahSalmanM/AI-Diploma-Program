"""
Unit 1 - Example 2: History of Artificial Intelligence
الوحدة 1 - مثال 2: تاريخ الذكاء الاصطناعي

This example demonstrates:
1. Key milestones in AI history
2. AI Winter periods
3. Modern AI renaissance
4. Timeline visualization
"""

import matplotlib.pyplot as plt
from datetime import datetime

print("=" * 60)
print("Example 2: History of Artificial Intelligence")
print("مثال 2: تاريخ الذكاء الاصطناعي")
print("=" * 60)

# AI History Timeline
# الخط الزمني لتاريخ الذكاء الاصطناعي
ai_timeline = [
    {
        "year": 1950,
        "event": "Turing Test proposed",
        "arabic": "اقتراح اختبار تورنغ",
        "significance": "Foundation of AI philosophy"
    },
    {
        "year": 1956,
        "event": "Dartmouth Conference - AI term coined",
        "arabic": "مؤتمر دارتموث - صياغة مصطلح الذكاء الاصطناعي",
        "significance": "Birth of AI as a field"
    },
    {
        "year": 1997,
        "event": "Deep Blue defeats world chess champion",
        "arabic": "ديب بلو يهزم بطل العالم في الشطرنج",
        "significance": "First major AI victory"
    },
    {
        "year": 2011,
        "event": "IBM Watson wins Jeopardy!",
        "arabic": "IBM Watson يفوز في Jeopardy!",
        "significance": "Natural language processing breakthrough"
    },
    {
        "year": 2016,
        "event": "AlphaGo defeats Go world champion",
        "arabic": "AlphaGo يهزم بطل العالم في Go",
        "significance": "Deep learning milestone"
    },
    {
        "year": 2022,
        "event": "ChatGPT released",
        "arabic": "إطلاق ChatGPT",
        "significance": "Generative AI revolution"
    }
]

print("\nAI History Timeline:")
print("الخط الزمني لتاريخ الذكاء الاصطناعي:")
print("-" * 60)

for milestone in ai_timeline:
    print(f"\n{milestone['year']}: {milestone['event']}")
    print(f"  {milestone['arabic']}")
    print(f"  Significance: {milestone['significance']}")

# AI Winter Periods
# فترات شتاء الذكاء الاصطناعي
print("\n" + "=" * 60)
print("AI Winter Periods")
print("فترات شتاء الذكاء الاصطناعي")
print("=" * 60)

ai_winters = [
    {
        "period": "1974-1980",
        "reason": "Overpromising and underdelivering",
        "arabic": "الوعود المفرطة وعدم الوفاء بها"
    },
    {
        "period": "1987-1993",
        "reason": "Expert systems limitations",
        "arabic": "قيود الأنظمة الخبيرة"
    }
]

for winter in ai_winters:
    print(f"\n{winter['period']}: {winter['reason']}")
    print(f"  {winter['arabic']}")

# Modern AI Renaissance
# نهضة الذكاء الاصطناعي الحديثة
print("\n" + "=" * 60)
print("Modern AI Renaissance (2010s-present)")
print("نهضة الذكاء الاصطناعي الحديثة (2010 حتى الآن)")
print("=" * 60)

renaissance_factors = [
    "Big Data availability",
    "Computational power increase (GPUs)",
    "Improved algorithms (Deep Learning)",
    "Open source frameworks (TensorFlow, PyTorch)",
    "Cloud computing accessibility"
]

print("\nKey Factors:")
print("العوامل الرئيسية:")
for i, factor in enumerate(renaissance_factors, 1):
    print(f"  {i}. {factor}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

