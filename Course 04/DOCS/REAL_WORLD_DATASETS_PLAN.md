# Real-World Datasets Integration Plan
## خطة تكامل مجموعات البيانات الواقعية

### Overview | نظرة عامة

This document outlines a comprehensive plan to integrate diverse real-world datasets across different fields and industries into Course 04. The goal is to expose students to various domains: finance, healthcare, e-commerce, social media, sports, education, and more.

---

## 🎯 Principles | المبادئ

1. **Diversity**: Datasets from different fields and industries
2. **Accessibility**: Easy to load (sklearn, pandas, URLs, or included files)
3. **Educational Value**: Clear learning objectives for each dataset
4. **Progressive Complexity**: Simpler datasets in early units, more complex in later units
5. **Real-World Relevance**: Datasets that students can relate to and use in projects

---

## 📊 Dataset Categories by Domain | فئات مجموعات البيانات حسب المجال

### 1. **Finance & Economics** | المالية والاقتصاد
- Stock prices, market data
- Credit risk, loan defaults
- Cryptocurrency prices
- Economic indicators

### 2. **Healthcare & Medical** | الرعاية الصحية والطبية
- Patient diagnosis
- Drug effectiveness
- Medical imaging (simplified)
- Health outcomes

### 3. **E-Commerce & Retail** | التجارة الإلكترونية والتجزئة
- Customer behavior
- Product recommendations
- Sales forecasting
- Customer segmentation

### 4. **Social Media & Technology** | وسائل التواصل الاجتماعي والتكنولوجيا
- User engagement
- Content recommendation
- Sentiment analysis
- User activity patterns

### 5. **Education** | التعليم
- Student performance
- Course completion
- Grade prediction
- Learning analytics

### 6. **Sports & Fitness** | الرياضة واللياقة البدنية
- Player performance
- Match outcomes
- Fitness tracking
- Team statistics

### 7. **Transportation & Logistics** | النقل واللوجستيات
- Traffic patterns
- Delivery optimization
- Public transport
- Route planning

### 8. **Energy & Environment** | الطاقة والبيئة
- Energy consumption
- Weather patterns
- Climate data
- Renewable energy

---

## 📚 Dataset Mapping by Unit | خريطة مجموعات البيانات حسب الوحدة

### **Unit 1: Basic Data Processing & Regression**

#### Current Status:
- ✅ Example 5: California Housing (Real Estate)

#### Proposed Additions:

| Example | Dataset | Domain | Description |
|---------|---------|--------|-------------|
| 01 | Sample Sales Data | E-Commerce | CSV with product sales, categories, prices |
| 02 | Credit Card Data | Finance | Credit card transactions (anonymized) |
| 04 | Student Grades | Education | Student performance data |
| 05 | California Housing ✅ | Real Estate | Already implemented |

**New Dataset Suggestions:**

1. **Sales Data (E-Commerce)**
   - Source: Generated realistic sales data or Kaggle
   - Fields: Product ID, Category, Price, Quantity Sold, Date, Customer Rating
   - Use: Data loading, exploration, basic statistics

2. **Student Performance (Education)**
   - Source: UCI ML Repository or generated
   - Fields: Study hours, attendance, previous grades, final grade
   - Use: Linear regression (predicting grades)

3. **Car Price Data (Automotive)**
   - Source: Kaggle or UCI ML Repository
   - Fields: Brand, Model, Year, Mileage, Price, Features
   - Use: Multiple linear regression

---

### **Unit 2: Advanced Regression**

#### Proposed Datasets:

| Example | Dataset | Domain | Description |
|---------|---------|--------|-------------|
| 01 | Boston Housing (Legacy) | Real Estate | Multiple features for house prices |
| 02 | Bike Sharing Demand | Transportation | Hourly bike rental counts |
| 03 | Energy Consumption | Energy | Building energy usage patterns |

**New Dataset Suggestions:**

1. **Bike Sharing Dataset (Transportation)**
   - Source: UCI ML Repository
   - Fields: Season, Weather, Temperature, Humidity, Windspeed, Rental Count
   - Use: Ridge/Lasso regression, feature importance

2. **Energy Consumption (Energy)**
   - Source: UCI ML Repository
   - Fields: Temperature, Humidity, Light, CO2, Energy Consumption
   - Use: Regularization techniques, feature selection

3. **House Prices (Multiple Features)**
   - Source: Kaggle House Prices
   - Fields: Size, Location, Age, Features, Price
   - Use: Advanced regression with many features

---

### **Unit 3: Classification**

#### Current Status:
- Likely uses Iris (if implemented)

#### Proposed Datasets:

| Example | Dataset | Domain | Description |
|---------|---------|--------|-------------|
| 01 | Breast Cancer Diagnosis | Healthcare | Benign vs Malignant tumors |
| 02 | Credit Card Fraud | Finance | Fraudulent vs Normal transactions |
| 03 | Email Spam | Technology | Spam vs Ham emails |
| 04 | Customer Churn | E-Commerce | Churned vs Active customers |
| 05 | Heart Disease | Healthcare | Heart disease prediction |

**New Dataset Suggestions:**

1. **Breast Cancer Wisconsin (Healthcare)**
   - Source: `sklearn.datasets.load_breast_cancer()`
   - Use: Logistic regression, binary classification

2. **Credit Card Fraud Detection (Finance)**
   - Source: Kaggle or generated realistic data
   - Fields: Transaction amount, time, location, fraud label
   - Use: Imbalanced classification, precision/recall

3. **Wine Quality (Food & Beverage)**
   - Source: UCI ML Repository
   - Fields: Chemical properties, quality rating
   - Use: Multi-class classification

4. **Diabetes Prediction (Healthcare)**
   - Source: Pima Indians Diabetes Dataset
   - Fields: Glucose, BMI, Age, Outcome
   - Use: Binary classification

5. **Spam Email (Technology)**
   - Source: SMS Spam Collection or Email dataset
   - Use: Text classification basics

---

### **Unit 4: Clustering**

#### Proposed Datasets:

| Example | Dataset | Domain | Description |
|---------|---------|--------|-------------|
| 01 | Customer Segmentation | E-Commerce | Shopping behavior clusters |
| 02 | Mall Customer Data | Retail | Customer spending patterns |
| 03 | Countries Data | Economics | Economic indicators clustering |
| 04 | Iris ✅ | Biology | Already standard |

**New Dataset Suggestions:**

1. **Mall Customers (Retail)**
   - Source: Kaggle
   - Fields: Age, Income, Spending Score
   - Use: K-Means clustering, customer segments

2. **Countries Data (Economics)**
   - Source: World Bank or UCI
   - Fields: GDP, Life Expectancy, Population, etc.
   - Use: Hierarchical clustering, country groups

3. **Sales Data Segmentation (E-Commerce)**
   - Source: Generated or Kaggle
   - Fields: Purchase frequency, amount, product categories
   - Use: Customer lifetime value clustering

---

### **Unit 5: Model Selection & Boosting**

#### Proposed Datasets:

| Example | Dataset | Domain | Description |
|---------|---------|--------|-------------|
| 01 | Housing Prices (Complex) | Real Estate | Many features, best model selection |
| 02 | Loan Default Prediction | Finance | Credit risk with multiple models |
| 03 | Employee Performance | HR | Performance prediction |

**New Dataset Suggestions:**

1. **Loan Default (Finance)**
   - Source: Kaggle or UCI
   - Fields: Credit history, income, loan amount, default status
   - Use: Hyperparameter tuning, model comparison

2. **Employee Performance (HR)**
   - Source: Generated realistic data
   - Fields: Experience, Education, Department, Performance Score
   - Use: Grid search, ensemble methods

---

## 🔧 Implementation Strategy | استراتيجية التنفيذ

### Phase 1: Quick Wins (Easy to Implement)

**Datasets Already Available in sklearn:**
```python
from sklearn.datasets import (
    load_breast_cancer,      # Healthcare - Classification
    load_wine,               # Food - Classification  
    load_iris,               # Biology - Clustering
    fetch_california_housing,# Real Estate - Regression ✅
    load_diabetes,           # Healthcare - Regression
)
```

### Phase 2: UCI ML Repository

**Easy to Load via URLs:**
- Wine Quality: https://archive.ics.uci.edu/ml/datasets/wine+quality
- Car Evaluation: https://archive.ics.uci.edu/ml/datasets/car+evaluation
- Student Performance: https://archive.ics.uci.edu/ml/datasets/student+performance

### Phase 3: Kaggle Datasets (Popular & Well-Documented)

**Recommended for Projects:**
- House Prices (Advanced)
- Credit Card Fraud Detection
- Customer Segmentation
- Sales Forecasting

### Phase 4: Generated Realistic Data

**For Exercises:**
- Sales data with realistic patterns
- Customer behavior data
- Time series data

---

## 📋 Detailed Dataset List | قائمة مفصلة بمجموعات البيانات

### **Regression Datasets**

| Dataset | Domain | Source | Size | Features | Best For |
|---------|--------|--------|------|----------|----------|
| California Housing ✅ | Real Estate | sklearn | 20K | 8 | Polynomial regression |
| Diabetes | Healthcare | sklearn | 442 | 10 | Linear regression |
| Boston Housing | Real Estate | sklearn (deprecated) | 506 | 13 | Multiple regression |
| Bike Sharing | Transportation | UCI | 17K | 16 | Time series, Ridge/Lasso |
| Energy Consumption | Energy | UCI | 19K | 28 | Regularization |
| Car Price | Automotive | Kaggle | ~10K | 10+ | Multiple regression |

### **Classification Datasets**

| Dataset | Domain | Source | Size | Classes | Best For |
|---------|--------|--------|------|---------|----------|
| Breast Cancer | Healthcare | sklearn | 569 | 2 | Logistic regression |
| Wine Quality | Food | UCI | 6K | 11 (quality) | Multi-class, Decision Trees |
| Iris ✅ | Biology | sklearn | 150 | 3 | Clustering, basic classification |
| Pima Diabetes | Healthcare | UCI | 768 | 2 | Binary classification |
| Credit Card Fraud | Finance | Kaggle | 284K | 2 | Imbalanced classes |
| Spam Email | Technology | UCI | 5K | 2 | Text classification |
| Customer Churn | E-Commerce | Generated/Kaggle | 10K | 2 | Business applications |

### **Clustering Datasets**

| Dataset | Domain | Source | Size | Features | Best For |
|---------|--------|--------|------|----------|----------|
| Mall Customers | Retail | Kaggle | 200 | 5 | K-Means, customer segments |
| Countries | Economics | World Bank/UCI | 200+ | 10+ | Hierarchical clustering |
| Wine | Food | sklearn | 178 | 13 | K-Means, quality groups |
| Iris ✅ | Biology | sklearn | 150 | 4 | Basic clustering |
| Customer Segmentation | E-Commerce | Generated | 1K | 8 | Real-world application |

---

## 🚀 Integration Steps | خطوات التكامل

### Step 1: Update Unit 1

**Files to Modify:**
- `unit1-data-processing/examples/01_data_loading_exploration.ipynb`
  - Add: Sales data example (E-Commerce)
  - Add: Student performance data (Education)

- `unit1-data-processing/examples/04_linear_regression.ipynb`
  - Keep: Current example or replace with Student Grades dataset

- `unit1-data-processing/examples/05_polynomial_regression.ipynb`
  - ✅ Already uses California Housing (Real Estate)

### Step 2: Update Unit 2

**Files to Modify:**
- `unit2-regression/examples/01_ridge_lasso_regression.ipynb`
  - Add: Bike Sharing dataset (Transportation)

- `unit2-regression/examples/02_cross_validation.ipynb`
  - Add: Energy Consumption dataset (Energy)

### Step 3: Update Unit 3

**Files to Modify:**
- `unit3-classification/examples/01_logistic_regression.ipynb`
  - Add: Breast Cancer dataset (Healthcare)

- `unit3-classification/examples/02_decision_trees.ipynb`
  - Add: Wine Quality dataset (Food & Beverage)

- `unit3-classification/examples/03_svm.ipynb`
  - Add: Credit Card Fraud dataset (Finance) - use subset for speed

### Step 4: Update Unit 4

**Files to Modify:**
- `unit4-clustering/examples/01_kmeans_clustering.ipynb`
  - Add: Mall Customers dataset (Retail)

- `unit4-clustering/examples/02_hierarchical_clustering.ipynb`
  - Add: Countries dataset (Economics)

### Step 5: Update Unit 5

**Files to Modify:**
- `unit5-model-selection/examples/01_grid_search.ipynb`
  - Add: Loan Default dataset (Finance)

- `unit5-model-selection/examples/02_boosting.ipynb`
  - Add: Employee Performance dataset (HR)

---

## 💻 Code Templates | قوالب الكود

### Template 1: Loading sklearn Dataset

```python
from sklearn.datasets import load_breast_cancer
import pandas as pd

# Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print(f"Dataset: {data.DESCR[:200]}...")
print(f"Shape: {df.shape}")
print(f"Features: {df.columns.tolist()}")
```

### Template 2: Loading from URL (UCI)

```python
import pandas as pd
import numpy as np

# Load from UCI URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')

print(f"Dataset: Wine Quality")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
```

### Template 3: Loading from Local CSV

```python
import pandas as pd

# Load local CSV file
df = pd.read_csv('data/mall_customers.csv')

# Display info
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)
print(f"\nMissing values:")
print(df.isnull().sum())
```

---

## 📊 Dataset Diversity Matrix | مصفوفة تنوع مجموعات البيانات

| Unit | Finance | Healthcare | E-Commerce | Education | Transportation | Energy | Real Estate | Food | Total |
|------|---------|------------|------------|-----------|----------------|--------|-------------|------|-------|
| Unit 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 ✅ | 0 | 4 |
| Unit 2 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 2 |
| Unit 3 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 5 |
| Unit 4 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| Unit 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **3** | **2** | **4** | **1** | **1** | **1** | **1** | **1** | **14** |

---

## ✅ Implementation Checklist | قائمة التحقق للتنفيذ

### Priority 1: High Impact, Easy Implementation
- [ ] Unit 3: Add Breast Cancer dataset (Healthcare)
- [ ] Unit 3: Add Wine Quality dataset (Food)
- [ ] Unit 4: Add Mall Customers dataset (Retail)
- [ ] Unit 1: Add Student Performance dataset (Education)

### Priority 2: Medium Impact
- [ ] Unit 2: Add Bike Sharing dataset (Transportation)
- [ ] Unit 3: Add Credit Card Fraud dataset (Finance)
- [ ] Unit 4: Add Countries dataset (Economics)
- [ ] Unit 5: Add Loan Default dataset (Finance)

### Priority 3: Advanced/Project Level
- [ ] Unit 5: Add Employee Performance dataset (HR)
- [ ] Create dataset download utility script
- [ ] Add dataset documentation for each unit

---

## 📝 Notes for Instructors | ملاحظات للمعلمين

1. **Start Simple**: Begin with sklearn datasets (easy to load)
2. **Progressive Complexity**: Introduce URL/local file datasets in later units
3. **Domain Relevance**: Choose datasets relevant to your student population
4. **Data Size**: Use subsets for faster computation during examples
5. **Documentation**: Always include dataset source and description

---

## 🔗 Useful Resources | موارد مفيدة

### Dataset Sources:
1. **sklearn.datasets**: Built-in, easy to use
2. **UCI ML Repository**: https://archive.ics.uci.edu/ml/index.php
3. **Kaggle Datasets**: https://www.kaggle.com/datasets
4. **Papers with Code Datasets**: https://paperswithcode.com/datasets

### Python Packages:
- `pandas`: For CSV/Excel loading
- `requests`: For downloading from URLs
- `sklearn.datasets`: For built-in datasets
- `seaborn`: Includes sample datasets (`sns.load_dataset()`)

---

## 📅 Timeline Suggestion | اقتراح الجدول الزمني

**Week 1-2**: Implement Priority 1 datasets
**Week 3-4**: Implement Priority 2 datasets  
**Week 5+**: Implement Priority 3 and create utilities

---

*Last Updated: [Current Date]*
*Status: Planning Phase*

