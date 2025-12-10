"""
Unit 4 - Exercise 1: Neural Networks Basics
الوحدة 4 - تمرين 1: أساسيات الشبكات العصبية

Complete the following exercises.
أكمل التمارين التالية.
"""

import numpy as np

# Exercise 1: Implement Activation Functions
# التمرين 1: تنفيذ دوال التنشيط
print("Exercise 1: Activation Functions")
print("التمرين 1: دوال التنشيط")
print("-" * 60)

def sigmoid(x):
    """
    TODO: Implement sigmoid activation function.
    TODO: نفذ دالة التنشيط السيجمويد.
    
    Formula: 1 / (1 + e^(-x))
    """
    # TODO: Implement sigmoid
    pass

def relu(x):
    """
    TODO: Implement ReLU activation function.
    TODO: نفذ دالة التنشيط ReLU.
    
    Formula: max(0, x)
    """
    # TODO: Implement ReLU
    pass

# Test activation functions
test_values = [-2, -1, 0, 1, 2]
print("\nTesting activation functions:")
for x in test_values:
    sig_result = sigmoid(x)
    relu_result = relu(x)
    print(f"x={x:3d}: sigmoid={sig_result:.3f}, ReLU={relu_result:.3f}")

# Exercise 2: Simple Perceptron for OR Gate
# التمرين 2: بيرسبترون بسيط لبوابة OR
print("\n" + "=" * 60)
print("Exercise 2: OR Gate Perceptron")
print("التمرين 2: بيرسبترون بوابة OR")
print("=" * 60)

# TODO: Create training data for OR gate
# TODO: أنشئ بيانات التدريب لبوابة OR
X_or = np.array([
    # TODO: Add OR gate inputs
])

y_or = np.array([
    # TODO: Add OR gate outputs
])

# TODO: Train a perceptron to learn OR gate
# TODO: درب بيرسبترون لتعلم بوابة OR

print("\n" + "=" * 60)
print("Exercises completed! Check solutions/ folder.")
print("تم إكمال التمارين! راجع مجلد solutions/.")
print("=" * 60)

