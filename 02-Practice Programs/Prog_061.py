# create a function that returns whether a number is even or odd.

def func(num):
    if num%2==0:
        return("Even")
    else:
        return("Odd")
number = int(input("Enter a number:"))
result = func(number)
print(result)