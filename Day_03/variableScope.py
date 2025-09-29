# Scope of variable in python 

x = 10  # Global variable

def test():
    x = 5 # Local variable
    print("Inside function, x =", x)

test()  # Calling the function
print("Outside function, x =", x)  # Accessing global variable
