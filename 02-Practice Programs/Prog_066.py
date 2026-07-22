# Create a local variable inside a function and print it. Then try to print it outside the function. Observe what happens.

def func():
    a = 10
    print(a)

func()

# print(a) 
# Error will occur because 'a' is a local variable.
# Local variables can only be accessed inside the function where they are created.
# To use its value outside the function, we can return it using the return statement.