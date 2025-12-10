"""
Unit 1 - Example 1: Generative vs Discriminative Models
الوحدة 1 - مثال 1: النماذج التوليدية مقابل التمييزية

This example demonstrates:
1. Difference between generative and discriminative models
2. Simple examples of each
3. When to use each type
"""

import numpy as np
from sklearn.naive_bayes import GaussianNB  # Generative
from sklearn.linear_model import LogisticRegression  # Discriminative

print("=" * 60)
print("Example 1: Generative vs Discriminative Models")
print("مثال 1: النماذج التوليدية مقابل التمييزية")
print("=" * 60)

# Sample data: Height and Weight to predict Gender
# بيانات نموذجية: الطول والوزن للتنبؤ بالجنس
print("\n1. Understanding the Difference")
print("فهم الفرق")
print("-" * 60)

difference_explanation = """
Generative Models (النماذج التوليدية):
- Learn P(X, Y) - joint probability of features and labels
- Can generate new data samples
- Examples: Naive Bayes, GANs, VAEs

Discriminative Models (النماذج التمييزية):
- Learn P(Y|X) - conditional probability of labels given features
- Focus on decision boundary
- Examples: Logistic Regression, SVM, Neural Networks
"""

print(difference_explanation)

# Example: Simple classification problem
print("\n" + "=" * 60)
print("2. Practical Example")
print("مثال عملي")
print("=" * 60)

# Generate sample data
# إنشاء بيانات نموذجية
np.random.seed(42)
n_samples = 100

# Male: taller and heavier on average
# الذكور: أطول وأثقل في المتوسط
male_height = np.random.normal(175, 7, n_samples // 2)
male_weight = np.random.normal(80, 10, n_samples // 2)
male_data = np.column_stack([male_height, male_weight])

# Female: shorter and lighter on average
# الإناث: أقصر وأخف في المتوسط
female_height = np.random.normal(165, 6, n_samples // 2)
female_weight = np.random.normal(65, 8, n_samples // 2)
female_data = np.column_stack([female_height, female_weight])

# Combine data
X = np.vstack([male_data, female_data])
y = np.array([0] * (n_samples // 2) + [1] * (n_samples // 2))

print(f"\nDataset created: {len(X)} samples")
print(f"Features: Height (cm), Weight (kg)")
print(f"Labels: 0 = Male, 1 = Female")

# Generative Model: Naive Bayes
print("\n" + "-" * 60)
print("Generative Model: Naive Bayes")
print("النموذج التوليدي: Naive Bayes")
print("-" * 60)

generative_model = GaussianNB()
generative_model.fit(X, y)
print("✓ Naive Bayes trained (learns P(X, Y))")
print("✓ تم تدريب Naive Bayes (يتعلم P(X, Y))")

# Discriminative Model: Logistic Regression
print("\n" + "-" * 60)
print("Discriminative Model: Logistic Regression")
print("النموذج التمييزي: الانحدار اللوجستي")
print("-" * 60)

discriminative_model = LogisticRegression()
discriminative_model.fit(X, y)
print("✓ Logistic Regression trained (learns P(Y|X))")
print("✓ تم تدريب الانحدار اللوجستي (يتعلم P(Y|X))")

# Make predictions
print("\n" + "=" * 60)
print("3. Predictions")
print("التوقعات")
print("=" * 60)

test_samples = np.array([
    [170, 75],  # Average
    [180, 85],  # Likely male
    [160, 60]   # Likely female
])

gen_predictions = generative_model.predict(test_samples)
disc_predictions = discriminative_model.predict(test_samples)

print("\nTest samples:")
for i, sample in enumerate(test_samples):
    gen_pred = "Male" if gen_predictions[i] == 0 else "Female"
    disc_pred = "Male" if disc_predictions[i] == 0 else "Female"
    print(f"\nSample {i+1}: Height={sample[0]}cm, Weight={sample[1]}kg")
    print(f"  Generative (Naive Bayes): {gen_pred}")
    print(f"  Discriminative (Logistic): {disc_pred}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

