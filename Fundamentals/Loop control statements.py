# Loop control statements are used to control the flow of a loop. They can be used to skip certain iterations of a loop or to exit a loop early.

# The break statement is used to exit a loop prematurely. When the break statement is executed, the loop will immediately terminate and the program will continue with the next statement after the loop.
#Example:
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# The continue statement is used to skip the current iteration of a loop and move on to the next iteration. When the continue statement is executed, the rest of the code inside the loop for that iteration will be skipped, and the loop will proceed to the next iteration.  
#Example:
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# The pass statement is a null statement that is used as a placeholder in situations where a statement is syntactically required but no action is needed. It does nothing and is often used in loops or functions that are not yet implemented.
#Example:
for i in range(1, 10):
    if i == 5:
        pass  # This is a placeholder for future code
    print(i)
    