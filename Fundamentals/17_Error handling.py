# ================================
# ERROR HANDLING
# ================================

# --------------------------------
# 1. Errors vs Exceptions
# --------------------------------

# Error:
# A problem in the program that stops execution.
# Example: SyntaxError (missing colon, wrong indentation, etc.)

# Exception:
# An error that occurs while the program is running.
# Exceptions can be handled using try and except.


# --------------------------------
# 2. try & except
# --------------------------------

# try:
# Code that may cause an exception.

# except:
# Executes only if an exception occurs.

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")


# --------------------------------
# 3. else
# --------------------------------

# else executes only if NO exception occurs.

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)


# --------------------------------
# 4. finally
# --------------------------------

# finally always executes,
# whether an exception occurs or not.
# Commonly used for closing files or releasing resources.

try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program Finished")


# --------------------------------
# 5. Common Exceptions
# --------------------------------

# ValueError
# Raised when the value is of the correct type,
# but the value itself is invalid.
# Example: Converting "abc" to int.

try:
    num = int("abc")
except ValueError:
    print("ValueError")


# TypeError
# Raised when an operation is performed
# on incompatible data types.
# Example: Adding a string and an integer.

try:
    result = "10" + 10
except TypeError:
    print("TypeError")


# IndexError
# Raised when accessing an invalid
# index of a list or tuple.

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("IndexError")


# KeyError
# Raised when trying to access
# a dictionary key that does not exist.

try:
    student = {"name": "Ayush"}
    print(student["age"])
except KeyError:
    print("KeyError")


# ZeroDivisionError
# Raised when dividing a number by zero.

try:
    print(10 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError")


# FileNotFoundError
# Raised when trying to open
# a file that does not exist.

try:
    file = open("abc.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError")


# --------------------------------
# 6. raise (Custom Exceptions)
# --------------------------------

# raise is used to manually create an exception.
# It allows you to stop the program and display
# your own custom error message.

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
