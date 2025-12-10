"""
Unit 4 - Example 1: Simple Perceptron
الوحدة 4 - مثال 1: البيرسبترون البسيط

This example demonstrates:
1. Perceptron implementation
2. Training a perceptron
3. Binary classification
4. Decision boundary visualization
"""

import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("Example 1: Simple Perceptron")
print("مثال 1: البيرسبترون البسيط")
print("=" * 60)

class SimplePerceptron:
    """
    Simple Perceptron for binary classification.
    بيرسبترون بسيط للتصنيف الثنائي.
    """
    
    def __init__(self, learning_rate=0.1, epochs=100):
        """
        Initialize perceptron.
        تهيئة البيرسبترون.
        
        Args:
            learning_rate: Learning rate (default: 0.1)
            epochs: Number of training iterations (default: 100)
        """
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
    
    def activation(self, x):
        """
        Step activation function.
        دالة التنشيط الخطوة.
        
        Returns 1 if x >= 0, else 0
        """
        return 1 if x >= 0 else 0
    
    def fit(self, X, y):
        """
        Train the perceptron.
        تدريب البيرسبترون.
        
        Args:
            X: Input features (n_samples, n_features)
            y: Target labels (0 or 1)
        """
        n_samples, n_features = X.shape
        
        # Initialize weights and bias
        # تهيئة الأوزان والانحياز
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        print("\nTraining Perceptron...")
        print("تدريب البيرسبترون...")
        
        for epoch in range(self.epochs):
            errors = 0
            for i in range(n_samples):
                # Forward pass
                # المرور الأمامي
                linear_output = np.dot(X[i], self.weights) + self.bias
                prediction = self.activation(linear_output)
                
                # Update weights if prediction is wrong
                # تحديث الأوزان إذا كانت التوقعات خاطئة
                error = y[i] - prediction
                if error != 0:
                    errors += 1
                    self.weights += self.learning_rate * error * X[i]
                    self.bias += self.learning_rate * error
            
            if errors == 0:
                print(f"  Converged at epoch {epoch + 1}")
                print(f"  تقارب في العصر {epoch + 1}")
                break
            
            if (epoch + 1) % 10 == 0:
                print(f"  Epoch {epoch + 1}: {errors} errors")
        
        print(f"\nTraining complete!")
        print(f"تم التدريب!")
        print(f"Final weights: {self.weights}")
        print(f"Final bias: {self.bias}")
    
    def predict(self, X):
        """
        Make predictions.
        عمل التوقعات.
        """
        predictions = []
        for i in range(len(X)):
            linear_output = np.dot(X[i], self.weights) + self.bias
            predictions.append(self.activation(linear_output))
        return np.array(predictions)

# Example: AND Gate
# مثال: بوابة AND
print("\n" + "=" * 60)
print("Example: AND Gate Classification")
print("مثال: تصنيف بوابة AND")
print("=" * 60)

# Training data for AND gate
# بيانات التدريب لبوابة AND
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])  # AND gate output

print("\nTraining Data:")
print("بيانات التدريب:")
print("Input | Output")
print("------|-------")
for i in range(len(X)):
    print(f"{X[i]}  |   {y[i]}")

# Create and train perceptron
# إنشاء وتدريب البيرسبترون
perceptron = SimplePerceptron(learning_rate=0.1, epochs=100)
perceptron.fit(X, y)

# Test the perceptron
# اختبار البيرسبترون
print("\n" + "=" * 60)
print("Testing Perceptron")
print("اختبار البيرسبترون")
print("=" * 60)

predictions = perceptron.predict(X)
print("\nPredictions:")
print("التوقعات:")
print("Input | Expected | Predicted | Correct")
print("------|----------|-----------|--------")
for i in range(len(X)):
    correct = "✓" if predictions[i] == y[i] else "✗"
    print(f"{X[i]}  |    {y[i]}     |     {predictions[i]}     |   {correct}")

accuracy = np.mean(predictions == y) * 100
print(f"\nAccuracy: {accuracy}%")
print(f"الدقة: {accuracy}%")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
