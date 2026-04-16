# -------------------------------
# FUNCTIONS IN PYTHON
# -------------------------------

# A function is a group of statements that performs a specific task.
# When a program becomes large and complex, it becomes difficult
# to understand and manage the code.
# Functions help in organizing code and allow reuse.

# -------------------------------
# FUNCTION DEFINITION (Syntax)
# -------------------------------

def func1():
    print("hello")

# This function prints "hello"


# -------------------------------
# FUNCTION CALL
# -------------------------------

# To call a function, we use its name followed by parentheses

func1()   # Output: hello


# -------------------------------
# FUNCTION DEFINITION EXPLAINED
# -------------------------------

# Function definition contains the actual set of instructions
# that are executed when the function is called.


# -------------------------------
# TYPES OF FUNCTIONS
# -------------------------------

# 1. Built-in Functions (already available in Python)
# Examples: len(), print(), range()

# 2. User-defined Functions (created by the user)
# Example: func1()


# -------------------------------
# FUNCTIONS WITH ARGUMENTS
# -------------------------------

# A function can take input values (arguments)

def greet(name):
    gr = "hello " + name
    return gr   # returns the result

a = greet("harry")

# Now 'a' contains "hello harry"


# -------------------------------
# DEFAULT PARAMETER VALUE
# -------------------------------

# A default value can be assigned to parameters

def greet(name="stranger"):
    print("hello " + name)

greet()         # Output: hello stranger
greet("harry")  # Output: hello harry


# -------------------------------
# RECURSION
# -------------------------------

# Recursion is when a function calls itself

# Example: Factorial
# factorial(n) = n * factorial(n-1)

def factorial(n):
    # Base condition (stops recursion)
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive call
        return n * factorial(n - 1)


# Example call
print(factorial(5))   # Output: 120