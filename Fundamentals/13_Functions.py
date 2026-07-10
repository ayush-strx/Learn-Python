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

#-------------------------------
# Return values in functions
#-------------------------------
# A function can return a value using the 'return' statement, This is useful when we want to use the result of a function in another part of the program.
# Example: A function that adds two numbers and returns the result

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

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

#-------------------------------
# Scope of variables in functions
#-------------------------------
#1.Local variables are defined inside a function and can only be accessed within that function.
def my_function():
    local_var = "I am local"
    print(local_var)

my_function()  # Output: I am local 

#2.Global variables are defined outside a function and can be accessed from anywhere in the program.
global_var = "I am global"
def my_function2():
    print(global_var)

my_function2()  # Output: I am global
