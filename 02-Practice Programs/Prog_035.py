# Find the sum of the first N natural numbers usinf for loop.

num = int(input("Enter the number:"))
sum = 0

for i in range(1, num+1):
    sum = sum + i

print("Sum =", sum)

