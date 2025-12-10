# Quiz 01: AI Foundations | اختبار 1: أساسيات الذكاء الاصطناعي
## AIAT 111 - Unit 1

**Time Limit:** 30 minutes | **الوقت المحدد:** 30 دقيقة  
**Total Points:** 100 points | **إجمالي النقاط:** 100 نقطة

---

## Part 1: Multiple Choice | الجزء 1: اختيار من متعدد
**(40 points | 40 نقطة)**

### Question 1 (10 points)
What is the main goal of Artificial Intelligence?

أ) To replace all human jobs  
ب) To simulate human intelligence in machines  
ج) To create robots only  
د) To eliminate human decision-making

**Answer:** ب

---

### Question 2 (10 points)
Which type of AI is currently achievable?

أ) General AI  
ب) Superintelligent AI  
ج) Narrow AI  
د) Self-aware AI

**Answer:** ج

---

### Question 3 (10 points)
What marked the "birth" of AI as a field?

أ) Turing Test (1950)  
ب) Dartmouth Conference (1956)  
ج) Deep Blue victory (1997)  
د) ChatGPT release (2022)

**Answer:** ب

---

### Question 4 (10 points)
Which is NOT an application of AI?

أ) Medical image analysis  
ب) Weather prediction  
ج) Making coffee manually  
د) Fraud detection

**Answer:** ج

---

## Part 2: Short Answer | الجزء 2: إجابة قصيرة
**(30 points | 30 نقطة)**

### Question 5 (15 points)
Explain the difference between Narrow AI and General AI. Give one example of each.

اشرح الفرق بين الذكاء الاصطناعي الضيق والعام. أعط مثالاً واحداً لكل منهما.

**Answer Key:**
- Narrow AI: Designed for specific tasks, currently achievable (e.g., Siri, image recognition)
- General AI: Human-level intelligence across all domains, not yet achieved

---

### Question 6 (15 points)
List three factors that contributed to the modern AI renaissance (2010s-present).

اذكر ثلاثة عوامل ساهمت في نهضة الذكاء الاصطناعي الحديثة.

**Answer Key:**
- Big Data availability
- Increased computational power (GPUs)
- Improved algorithms (Deep Learning)
- Open source frameworks
- Cloud computing

---

## Part 3: Code Writing | الجزء 3: كتابة الكود
**(30 points | 30 نقطة)**

### Question 7 (30 points)
Write a simple rule-based AI system that recommends a study schedule based on:
- Time available (hours: 1-2, 3-4, 5+)
- Subject difficulty (easy, medium, hard)
- Energy level (low, medium, high)

اكتب نظام ذكاء اصطناعي بسيط قائم على القواعد يوصي بجدول دراسة بناءً على:
- الوقت المتاح (ساعات: 1-2، 3-4، 5+)
- صعوبة المادة (سهلة، متوسطة، صعبة)
- مستوى الطاقة (منخفض، متوسط، عالي)

**Sample Answer:**
```python
def recommend_study_schedule(time_available, difficulty, energy_level):
    if time_available == "1-2":
        if difficulty == "easy" and energy_level in ["medium", "high"]:
            return "Focus on one easy topic"
        else:
            return "Take a break, study later"
    elif time_available == "3-4":
        if energy_level == "high":
            return "Study hard topics"
        elif energy_level == "medium":
            return "Study medium difficulty topics"
        else:
            return "Review easy topics"
    else:  # 5+ hours
        if energy_level == "high":
            return "Full study day - mix of all topics"
        else:
            return "Break into sessions with rest"
```

---

## Answer Key | مفتاح الإجابات

1. ب  
2. ج  
3. ب  
4. ج  
5. See answer key above  
6. See answer key above  
7. See sample code above

---

**For:** AIAT 111 - Introduction to AI Applications and Concepts
