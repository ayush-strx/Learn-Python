# Ask the user to enter numbers continuously. Stop the program when the user enters 0.

while True:
    num = int(input("Enter the number: "))

    if num == 0:
        break

    print(num)