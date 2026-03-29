# Loops in Python:

# For loops are used to iterate over a sequence (such as a list, tuple, or string).
#Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# While loops are used to execute a block of code as long as a specified condition is true.
#Example:
i = 1
while i <= 5:
    print(i)
    i += 1

# Nested loops are loops inside loops. The inner loop will be executed for each iteration of the outer loop.
#Example:   
for i in range(1, 4):
    for j in range(1, 4):
        print("i:" ,{i}, "j:", {j})