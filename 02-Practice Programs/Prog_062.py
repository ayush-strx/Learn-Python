# Create a function that returns the factorial of a number.

def fact(num2):
    fact = 1
    for i in range(1,num2+1):
        fact = fact* i
    return fact    
num1 = int(input('Enter a number:'))

result = fact(num1)
print(result)