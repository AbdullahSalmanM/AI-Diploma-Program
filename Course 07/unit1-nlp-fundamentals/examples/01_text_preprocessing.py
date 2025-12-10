"""
Unit 1 - Example 1: Text Preprocessing
الوحدة 1 - مثال 1: معالجة النص مسبقاً

This example demonstrates basic text preprocessing techniques.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
except:
    pass

print("=" * 60)
print("Example 1: Text Preprocessing")
print("مثال 1: معالجة النص مسبقاً")
print("=" * 60)

# Sample text
# نص نموذجي
text = """
Natural Language Processing (NLP) is a branch of artificial intelligence 
that helps computers understand, interpret and manipulate human language. 
NLP draws from many disciplines, including computer science and computational 
linguistics, in its pursuit to fill the gap between human communication and 
computer understanding.
"""

print("\nOriginal Text:")
print("النص الأصلي:")
print(text)

# 1. Lowercasing
# تحويل إلى أحرف صغيرة
text_lower = text.lower()
print("\n1. Lowercased:")
print("1. تحويل إلى أحرف صغيرة:")
print(text_lower[:100] + "...")

# 2. Remove punctuation and special characters
# إزالة علامات الترقيم والأحرف الخاصة
text_clean = re.sub(r'[^\w\s]', '', text_lower)
print("\n2. Removed punctuation:")
print("2. إزالة علامات الترقيم:")
print(text_clean[:100] + "...")

# 3. Tokenization
# التقطيع
tokens = word_tokenize(text_clean)
print("\n3. Tokenized:")
print("3. التقطيع:")
print(f"Number of tokens: {len(tokens)}")
print(f"First 10 tokens: {tokens[:10]}")

# 4. Remove stop words
# إزالة الكلمات الوظيفية
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
print("\n4. Removed stop words:")
print("4. إزالة الكلمات الوظيفية:")
print(f"Tokens before: {len(tokens)}, After: {len(filtered_tokens)}")
print(f"Filtered tokens: {filtered_tokens[:10]}")

# 5. Stemming
# التصريف
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered_tokens]
print("\n5. Stemmed:")
print("5. التصريف:")
print(f"Example: {filtered_tokens[:5]} -> {stemmed[:5]}")

# 6. Lemmatization
# الاشتقاق
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("\n6. Lemmatized:")
print("6. الاشتقاق:")
print(f"Example: {filtered_tokens[:5]} -> {lemmatized[:5]}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

