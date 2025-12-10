"""
Unit 1 - Example 1: Simple Neural Network with Keras
الوحدة 1 - مثال 1: شبكة عصبية بسيطة باستخدام Keras

This example demonstrates:
1. Building a simple neural network
2. Training on a dataset
3. Making predictions
4. Evaluating the model
"""

print("=" * 60)
print("Example 1: Simple Neural Network with Keras")
print("مثال 1: شبكة عصبية بسيطة باستخدام Keras")
print("=" * 60)

# Note: This example shows the structure. Actual implementation requires TensorFlow.
# ملاحظة: هذا المثال يوضح الهيكل. التنفيذ الفعلي يتطلب TensorFlow.

print("\nNeural Network Structure:")
print("هيكل الشبكة العصبية:")
print("-" * 60)

network_structure = """
Model: Sequential
├── Input Layer: 784 neurons (for 28x28 images)
├── Hidden Layer 1: 128 neurons, ReLU activation
├── Hidden Layer 2: 64 neurons, ReLU activation
└── Output Layer: 10 neurons, Softmax activation (for 10 classes)
"""

print(network_structure)

print("\nCode Structure (using Keras):")
print("هيكل الكود (باستخدام Keras):")
print("-" * 60)

code_example = """
from tensorflow import keras
from tensorflow.keras import layers

# Create model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy}')
"""

print(code_example)

print("\nKey Concepts:")
print("المفاهيم الرئيسية:")
print("-" * 60)
concepts = {
    "Dense Layer": "Fully connected layer where each neuron connects to all neurons in next layer",
    "ReLU": "Rectified Linear Unit - activation function that outputs max(0, x)",
    "Softmax": "Activation function for multi-class classification",
    "Adam Optimizer": "Adaptive learning rate optimization algorithm",
    "Epochs": "Number of times the model sees the entire training dataset"
}

for concept, explanation in concepts.items():
    print(f"\n{concept}:")
    print(f"  {explanation}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: Install TensorFlow to run actual code:")
print("pip install tensorflow")

