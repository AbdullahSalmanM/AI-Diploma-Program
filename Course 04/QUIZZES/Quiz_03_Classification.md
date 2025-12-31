# Quiz 03: Classification Techniques | اختبار 03: تقنيات التصنيف

## Instructions | التعليمات
- **Time Limit**: 40 minutes
- **Total Points**: 60 points
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: Classification Algorithms (20 points)

### Question 1 (5 points)
What is the main difference between regression and classification?
- A) Regression predicts continuous values, classification predicts categories
- B) Classification predicts continuous values, regression predicts categories
- C) There is no difference
- D) Regression uses neural networks, classification uses trees


---

### Question 2 (5 points)
Which algorithm uses a sigmoid function to output probabilities?
- A) Decision Tree
- B) Logistic Regression
- C) K-Nearest Neighbors
- D) Support Vector Machine


---

### Question 3 (5 points)
What is the main advantage of Decision Trees?
- A) They are always the most accurate
- B) They are easy to interpret and visualize
- C) They work best with large datasets
- D) They don't require feature scaling


---

### Question 4 (5 points)
What does SVM (Support Vector Machine) try to find?
- A) The best decision boundary that maximizes the margin
- B) The most common class
- C) The average of all features
- D) The correlation between features


---

## Part 2: Evaluation Metrics (20 points)

### Question 5 (5 points)
What does accuracy measure?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall


---

### Question 6 (5 points)
What is precision?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall


---

### Question 7 (5 points)
What is recall?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall


---

### Question 8 (5 points)
What does F1-score represent?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall


---

## Part 3: Confusion Matrix and ROC (20 points)

### Question 9 (5 points)
In a confusion matrix, what does True Positive (TP) represent?
- A) Correctly predicted negative cases
- B) Correctly predicted positive cases
- C) Incorrectly predicted negative cases
- D) Incorrectly predicted positive cases


---

### Question 10 (5 points)
What does False Positive (FP) represent in a confusion matrix?
- A) Model predicted Class 1, but actual is Class 0 (false alarm)
- B) Model predicted Class 0, but actual is Class 1 (missed detection)
- C) Model correctly predicted Class 1
- D) Model correctly predicted Class 0


---

### Question 11 (5 points)
What does False Negative (FN) represent in a confusion matrix?
- A) Model predicted Class 1, but actual is Class 0 (false alarm)
- B) Model predicted Class 0, but actual is Class 1 (missed detection)
- C) Model correctly predicted Class 1
- D) Model correctly predicted Class 0


---

### Question 12 (5 points)
What does AUC (Area Under Curve) measure in ROC analysis?
- A) The accuracy of the model
- B) The model's ability to distinguish between classes
- C) The precision of the model
- D) The recall of the model


---

## Part 4: Logistic Regression Details (10 points)

### Question 13 (5 points)
When are classification metrics (accuracy, precision, recall) calculated?
- A) Before training the model
- B) During training
- C) After training, on test data
- D) Before loading the data


---

### Question 14 (5 points)
What is the difference between `.predict()` and `.predict_proba()` in logistic regression?
- A) `.predict()` returns probabilities, `.predict_proba()` returns classes
- B) `.predict()` returns classes (0 or 1), `.predict_proba()` returns probabilities (0-1)
- C) They are the same
- D) `.predict()` is for training, `.predict_proba()` is for testing


---

## Answer Key | مفتاح الإجابات

### Part 1: Classification Algorithms
1. **A** - Regression predicts continuous values, classification predicts categories
2. **B** - Logistic Regression uses sigmoid function
3. **B** - Decision Trees are easy to interpret and visualize
4. **A** - SVM finds the best decision boundary that maximizes the margin

### Part 2: Evaluation Metrics
5. **A** - Accuracy measures the proportion of correctly classified instances
6. **B** - Precision is the proportion of positive predictions that are correct
7. **C** - Recall is the proportion of actual positives that are correctly identified
8. **D** - F1-score is the harmonic mean of precision and recall

### Part 3: Confusion Matrix and ROC
9. **B** - True Positive (TP) represents correctly predicted positive cases
10. **A** - False Positive (FP) is when model predicted Class 1, but actual is Class 0 (false alarm)
11. **B** - False Negative (FN) is when model predicted Class 0, but actual is Class 1 (missed detection)
12. **B** - AUC measures the model's ability to distinguish between classes

### Part 4: Logistic Regression Details
13. **C** - Metrics are calculated after training, on test data
14. **B** - `.predict()` returns classes (0 or 1), `.predict_proba()` returns probabilities (0-1)


---

**Good luck!** 🍀  
**حظاً موفقاً!**

