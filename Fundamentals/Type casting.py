# Type Casting 
# Type casting is the process of converting a variable from one data type to another.
# In Python, you can use built-in functions to perform type casting.  
      
# Example of type casting:
# Converting a string to an integer
num_str = "10"
num_int = int(num_str)  # Type casting from string to integer
print(num_int)  # Output: 10

# Converting an integer to a string
num = 10
num_str = str(num)  # Type casting from integer to string
print(num_str)  # Output: "10"

# Converting a float to an integer
float_num = 10.5
int_num = int(float_num)  # Type casting from float to integer
print(int_num)  # Output: 10

# Converting an integer to a float
num = 10
float_num = float(num)  # Type casting from integer to float
print(float_num)  # Output: 10.0


#Type () function is used to check the data type of a variable or value.
# Example of using type() function:
num = 10
print(type(num))  # Output:<class 'int'>
name = "Ayush"
print(type(name))  # Output: <class 'str'>
pi = 3.14
print(type(pi))  # Output: <class 'float'>      
is_student = True
print(type(is_student))  # Output: <class 'bool'>
