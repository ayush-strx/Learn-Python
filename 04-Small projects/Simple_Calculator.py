def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    print("<<---------- Simple Calculator ---------->>")

    operand1 = int(input("Enter the first number: "))
    operand2 = int(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("a: +")
    print("b: -")
    print("c: *")
    print("d: /")

    operator = input("Enter your choice: ")

    if operator == "a":
        print("Result:", add(operand1, operand2))
    elif operator == "b":
        print("Result:", subtract(operand1, operand2))
    elif operator == "c":
        print("Result:", multiply(operand1, operand2))
    elif operator == "d":
        if operand2 == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result:", divide(operand1, operand2))
    else:
        print("Invalid Choice")

main()