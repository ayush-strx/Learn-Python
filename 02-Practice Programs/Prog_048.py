# Ask the user to enter 5 numbers. Skip negative numbers and print only positive numbers.

for i in range(5):
    n = int(input("Enter the number:"))
    if n<0:
        continue
    print(n)


