# Calculator using functions
def add(x, y):
    """Return the sum of x and y."""
    return x + y
def subtract(x, y):
    """Return the difference of x and y."""
    return x - y
def multiply(x, y):
    """Return the product of x and y."""
    return x * y
def divide(x, y):   
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

print("**__Welcome to the Calculator!__**")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid choice! Please select a valid operation.")

