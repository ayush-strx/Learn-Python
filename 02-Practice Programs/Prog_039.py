# Print the squares of numbers from 1 to N using for loop.

num = int(input("Enter the number:"))

for i in range(1,num+1):
    squ = i * i
    print(i , "*" , i , "=", squ)