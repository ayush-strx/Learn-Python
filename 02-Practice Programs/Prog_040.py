# Print the cubes of numbers from 1 to N using while loop.

num = int(input("Enter the number:"))

i = 1
while i<= num:
    cub = i * i * i
    print(i , "*" , i , "*" , i ,"=", cub)
    i+=1
    