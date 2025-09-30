# Contact book application in Python using a dictionary to store contacts

print("**__Welcome to the Contact Book Application!__**")

contact_book = {}

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = int(input("Enter contact phone number: "))
        contact_book[name] = phone 
        print(f"Contact {name} added.")

    elif choice == '2':
        if contact_book:
            print("\nContact List:")
            for name, phone in contact_book.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    elif choice == '3':
        name = input("Enter contact name to search: ")
        if name in contact_book:
            print(f"{name}: {contact_book[name]}")
        else:
            print(f"Contact {name} not found.")

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")
    
    elif choice == '5':
        print("Exiting the Contact Book Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")