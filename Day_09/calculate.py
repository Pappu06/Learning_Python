print("Enter first number: ")

num1 = int(input())

print("Enter second number: ")

num2 = int(input())

print("Enter operation (+, -, *, /): ")

operation = input()

if operation == "+":
    result = num1 + num2
    print("Result: ", result)

elif operation == "-":
    result = num1 - num2
    print("Result: ", result)

elif operation == "*":
    result = num1 * num2
    print("Result: ", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid operation.")

