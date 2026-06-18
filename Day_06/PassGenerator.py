# Password Generator Project
import random
import string

# function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def strong_password():
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)
    others = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 8))
    
    password_list = list(upper + lower + digit + symbol + others)   
    random.shuffle(password_list)
    return ''.join(password_list)

# main function
print("Welcome to the Password Generator!")

while True:
    print("\nChoose an option:")
    print("1. Generate a simple password")
    print("2. Generate a strong password")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        length = int(input("Enter the desired password length: "))
        print("Generated Password:", generate_password(length))  

    elif choice == '2':
        print("Generated Strong Password:", strong_password())

    elif choice == '3':
        print("Exiting the Password Generator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
