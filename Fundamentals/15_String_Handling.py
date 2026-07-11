# ================================
# STRING HANDLING
# ================================

# --------------------------------
# 1. String Indexing & Slicing
# --------------------------------

# A string is a sequence of characters enclosed in quotes.

text = "Python"

# Indexing
print(text[0])   # P
print(text[2])   # t
print(text[-1])  # n
print(text[-2])  # o

# Slicing
# Syntax:
# string[start:end:step]

print(text[0:3])   # Pyt
print(text[2:6])   # thon
print(text[:4])    # Pyth
print(text[3:])    # hon
print(text[::2])   # Pto
print(text[::-1])  # nohtyP


# --------------------------------
# 2. String Methods
# --------------------------------

# upper() - Converts all letters to uppercase

text = "python"
print(text.upper())  # PYTHON


# lower() - Converts all letters to lowercase

text = "PYTHON"
print(text.lower())  # python


# split() - Splits a string into a list

text = "Python is easy"
print(text.split())  # ['Python', 'is', 'easy']

text = "Apple,Mango,Banana"
print(text.split(","))  # ['Apple', 'Mango', 'Banana']


# join() - Joins list elements into a single string

words = ["Python", "is", "easy"]

print(" ".join(words))  # Python is easy
print("-".join(words))  # Python-is-easy


# replace() - Replaces one substring with another

text = "I like Java"
print(text.replace("Java", "Python"))  # I like Python


# strip() - Removes spaces from both ends

text = "   Python   "
print(text.strip())  # Python


# --------------------------------
# 3. String Formatting
# --------------------------------

# f-Strings (Recommended)

name = "Ayush"
age = 18

print(f"My name is {name} and I am {age} years old.")


# .format() (Not recommended)

print("My name is {} and I am {} years old.".format(name, age))

# Numbered placeholders
print("Name: {0}, Age: {1}".format("Ayush", 18))

# Named placeholders
print("Name: {name}, Age: {age}".format(name="Ayush", age=18))