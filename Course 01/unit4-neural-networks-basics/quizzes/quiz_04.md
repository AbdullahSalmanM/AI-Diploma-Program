# Quiz 04: Neural Networks Basics | اختبار 4: أساسيات الشبكات العصبية
## AIAT 111 - Unit 4

**Time Limit:** 45 minutes  
**Total Points:** 100 points

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
A perceptron can solve:

أ) Only linearly separable problems  
ب) All classification problems  
ج) Only regression problems  
د) All problems

**Answer:** أ

---

### Question 2 (10 points)
The activation function in a perceptron is:

أ) Linear  
ب) Step function  
ج) Sigmoid  
د) Any function

**Answer:** ب

---

## Part 2: Code Writing (30 points)

### Question 3 (30 points)
Complete the perceptron prediction function:

```python
def predict(self, X):
    # TODO: Implement prediction
    pass
```

**Answer Key:**
```python
def predict(self, X):
    return [self.activation(np.dot(x, self.weights) + self.bias) 
            for x in X]
```

---

**For:** AIAT 111 - Introduction to AI Applications and Concepts

