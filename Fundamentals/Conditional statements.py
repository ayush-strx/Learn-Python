# Conditional Statements in Python:

# If statements are used to execute a block of code only if a specified condition is true. #Example:

age = 18
if age >= 18:
    print("You are an adult.")

# If-else statements allow you to execute one block of code if a condition is true and another block of code if the condition is false. 
#Example:
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Elif statements (short for "else if") allow you to check multiple conditions sequentially.
#Example:
age = 65
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Nested if statements allow you to check for multiple conditions within another If-else condition.
#Example:
number = 10
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

