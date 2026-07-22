# Find the sum of the first N natural numbers using while loop.

num = int(input("Enter the number:"))
sum = 0

i = 1
while i<= num:
    sum = sum + i
    i+=1

print("Sum =", sum)