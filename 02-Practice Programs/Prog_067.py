# Write a recursive function to print numbers from 5 to 1.

def countdown(n):
    if n == 0:
        return
    
    print(n)
    countdown(n-1)


countdown(5)