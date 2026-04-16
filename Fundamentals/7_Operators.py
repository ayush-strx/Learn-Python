# 1.Arithmetic Operators:
# These operators are used to perform mathematical operations on numbers. Examples : +, -, *, /, %, **, //    
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# 2.Comparison Operators:
# These operators are used to compare two values and return a boolean result (True or False). Examples : ==, !=, >, <, >=, <= , =
x = 10
y = 20      
print(x == y)  # Equal to
print(x != y)  # Not equal to       
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to

# 3.Logical Operators:
# These operators are used to combine multiple boolean expressions and return a boolean result. Examples include logical AND, logical OR, and logical NOT.
is_student = True
is_adult = False        
print(is_student and is_adult)  # Logical AND
print(is_student or is_adult)   # Logical OR
print(not is_student)          # Logical NOT

# 4.Assignment Operators:
# These operators are used to assign values to variables. Examples : =, +=, -=, *=, /=, %=, **=, //=

a = 10

a += 5  # a = a + 5
print(a)  # Output: 15
a -= 3  # a = a - 3
print(a)  # Output: 12
a *= 2  # a = a * 2 
print(a)  # Output: 24
a /= 4  # a = a / 4
print(a)  # Output: 6.0
a %= 5  # a = a % 5
print(a)  # Output: 1.0
a **= 3 # a = a ** 3
print(a)  # Output: 1.0
a //= 2 # a = a // 2
print(a)  # Output: 0.0

# 5.Bitwise Operators:
# These operators are used to perform bitwise operations on binary numbers. Examples include bitwise AND, bitwise OR, bitwise XOR, bitwise NOT, left shift, and right shift.
x = 5  # In binary: 0101
y = 3  # In binary: 0011
print(x & y)  # Bitwise AND (0101 & 0011 = 0001) Output: 1
print(x | y)  # Bitwise OR (0101 | 0011 = 0111) Output: 7
print(x ^ y)  # Bitwise XOR (0101 ^ 0011 = 0110) Output: 6
print(~x)     # Bitwise NOT (~0101 = 1010) Output: -6
print(x << 1) # Left shift (0101 << 1 = 1010) Output: 10
print(x >> 1) # Right shift (0101 >> 1 = 0010) Output: 2

# 6.Membership Operators:
# These operators are used to check if a value is present in a sequence (like a list or a string). Examples include in and not in.
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # Output: True
print(6 not in my_list)  # Output: True
my_string = "Hello, Python!"
print("Python" in my_string)  # Output: True   
print("Java" not in my_string) # Output: True

# 7.Identity Operators:
# These operators are used to compare the memory locations of two objects. Examples include is and is not.
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # Output: False
print(a is c)  # Output: True
print(a is not b)  # Output: True   
print(a is not c)  # Output: False

