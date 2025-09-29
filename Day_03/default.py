# Default parameters in functions
# Default parameters allow you to define a function with default values for some parameters.

def greet(name="Guest"):
    print(f"Hello, {name}! Welcome to Python")

greet()  # Uses default value
greet("Pappu")  # Overrides default value