num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while True:
    operation = input("Enter operation (+, -, *, /) or (exit) : ")

    # conditional operations
    if operation == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    elif operation == '+': #for addition
        result = num1 + num2
        print("Result:", result)
    elif operation == '-': #for subtraction
        result = num1 - num2
        print("Result:", result)
    elif operation == '*': #for multiplication
        result = num1 * num2
        print("Result:", result)
    elif operation == '/': #for division
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            result = "Error! Division by zero."
            print("Result:", result)
    else:
        result = "Invalid operation!"
        print("Result:", result)
