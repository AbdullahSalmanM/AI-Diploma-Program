"""
Unit 4 - Example 1: Simple Perceptron
الوحدة 4 - مثال 1: البيرسبترون البسيط

This example demonstrates a simple perceptron implementation.
"""

import numpy as np

class Perceptron:
    """Simple perceptron for binary classification."""
    
    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
    
    def activation(self, x):
        """Step activation function."""
        return 1 if x >= 0 else 0
    
    def fit(self, X, y):
        """Train the perceptron."""
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for epoch in range(self.epochs):
            for i in range(len(X)):
                prediction = self.activation(
                    np.dot(X[i], self.weights) + self.bias
                )
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error
    
    def predict(self, X):
        """Make predictions."""
        return [self.activation(np.dot(x, self.weights) + self.bias) 
                for x in X]

# Example
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # AND gate

perceptron = Perceptron()
perceptron.fit(X, y)
predictions = perceptron.predict(X)

print("Predictions:", predictions)

