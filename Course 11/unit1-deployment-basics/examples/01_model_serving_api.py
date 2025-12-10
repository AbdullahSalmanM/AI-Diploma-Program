"""
Unit 1 - Example 1: Model Serving with REST API
الوحدة 1 - مثال 1: تقديم النموذج باستخدام REST API

This example demonstrates:
1. Saving and loading a model
2. Creating a REST API endpoint
3. Serving predictions via API
"""

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

print("=" * 60)
print("Example 1: Model Serving with REST API")
print("مثال 1: تقديم النموذج باستخدام REST API")
print("=" * 60)

# 1. Train and Save Model
# تدريب وحفظ النموذج
print("\n1. Training and Saving Model")
print("تدريب وحفظ النموذج")
print("-" * 60)

# Create sample data
X, y = make_classification(n_samples=100, n_features=4, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

print("✓ Model trained successfully")
print("✓ تم تدريب النموذج بنجاح")

# Save model
model_filename = 'trained_model.pkl'
joblib.dump(model, model_filename)
print(f"✓ Model saved to {model_filename}")
print(f"✓ تم حفظ النموذج في {model_filename}")

# Load model
loaded_model = joblib.load(model_filename)
print("✓ Model loaded successfully")
print("✓ تم تحميل النموذج بنجاح")

# 2. API Structure (using Flask)
# هيكل API (باستخدام Flask)
print("\n" + "=" * 60)
print("2. REST API Structure")
print("هيكل REST API")
print("=" * 60)

api_code = """
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model at startup
model = joblib.load('trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].tolist()
    
    return jsonify({
        'prediction': int(prediction),
        'probability': probability
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""

print(api_code)

# 3. Example API Request
# مثال على طلب API
print("\n" + "=" * 60)
print("3. Example API Request")
print("مثال على طلب API")
print("=" * 60)

example_request = """
POST http://localhost:5000/predict
Content-Type: application/json

{
    "features": [0.5, 0.3, 0.8, 0.2]
}
"""

print(example_request)

example_response = """
Response:
{
    "prediction": 1,
    "probability": [0.2, 0.8]
}
"""

print(example_response)

# Test the loaded model
print("\n" + "=" * 60)
print("4. Testing Loaded Model")
print("اختبار النموذج المحمّل")
print("=" * 60)

test_sample = np.array([[0.5, 0.3, 0.8, 0.2]])
prediction = loaded_model.predict(test_sample)
probability = loaded_model.predict_proba(test_sample)

print(f"\nTest sample: {test_sample[0]}")
print(f"Prediction: {prediction[0]}")
print(f"Probability: {probability[0]}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: Install Flask to run API:")
print("pip install flask")

