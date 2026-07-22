# Find the factorial of a number using while loop.

num = int(input("Enter the number:"))
fact = 1
i = 1
while i<=num:
    fact = fact*i
    i+=1
print(fact)
