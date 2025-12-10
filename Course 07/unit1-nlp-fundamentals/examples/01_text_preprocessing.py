"""
Unit 1 - Example 1: Text Preprocessing
الوحدة 1 - مثال 1: معالجة النص مسبقاً

This example demonstrates:
1. Text tokenization
2. Text normalization
3. Stop word removal
4. Stemming and lemmatization
"""

import re
import string
from collections import Counter

print("=" * 60)
print("Example 1: Text Preprocessing")
print("مثال 1: معالجة النص مسبقاً")
print("=" * 60)

# Sample text
# نص نموذجي
sample_text = """
Natural Language Processing (NLP) is a branch of artificial intelligence
that helps computers understand, interpret, and manipulate human language.
NLP combines computational linguistics with machine learning.
"""

print("\nOriginal Text:")
print("النص الأصلي:")
print(sample_text)

# 1. Tokenization
# التقطيع
print("\n" + "=" * 60)
print("1. Tokenization")
print("التقطيع")
print("=" * 60)

def simple_tokenize(text):
    """
    Simple tokenization by splitting on whitespace.
    تقطيع بسيط بتقسيم على المسافات البيضاء.
    """
    # Remove extra whitespace and split
    tokens = text.lower().split()
    return tokens

tokens = simple_tokenize(sample_text)
print(f"\nTokens: {tokens}")
print(f"Number of tokens: {len(tokens)}")

# 2. Remove Punctuation
# إزالة علامات الترقيم
print("\n" + "=" * 60)
print("2. Remove Punctuation")
print("إزالة علامات الترقيم")
print("=" * 60)

def remove_punctuation(text):
    """
    Remove punctuation from text.
    إزالة علامات الترقيم من النص.
    """
    return text.translate(str.maketrans('', '', string.punctuation))

cleaned_text = remove_punctuation(sample_text)
print(f"\nCleaned text:\n{cleaned_text}")

# 3. Stop Word Removal
# إزالة الكلمات الوظيفية
print("\n" + "=" * 60)
print("3. Stop Word Removal")
print("إزالة الكلمات الوظيفية")
print("=" * 60)

# Common English stop words
# الكلمات الوظيفية الشائعة في الإنجليزية
stop_words = {'is', 'a', 'the', 'that', 'this', 'with', 'and', 'or', 'but'}

def remove_stop_words(tokens, stop_words):
    """
    Remove stop words from tokens.
    إزالة الكلمات الوظيفية من الرموز.
    """
    return [token for token in tokens if token not in stop_words]

filtered_tokens = remove_stop_words(tokens, stop_words)
print(f"\nTokens after stop word removal: {filtered_tokens}")

# 4. Word Frequency
# تكرار الكلمات
print("\n" + "=" * 60)
print("4. Word Frequency Analysis")
print("تحليل تكرار الكلمات")
print("=" * 60)

word_freq = Counter(filtered_tokens)
print("\nWord Frequencies:")
print("تكرار الكلمات:")
for word, freq in word_freq.most_common():
    print(f"  {word}: {freq}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
