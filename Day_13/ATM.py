initial_balance = 1000

while True:
    print("==== ATM Menu ====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ") 

    if choice == '1':
        print(f"Your current balance is: {initial_balance}")
    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            initial_balance += deposit_amount
            print(f"{deposit_amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    elif choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if 0 < withdraw_amount <= initial_balance:
            initial_balance -= withdraw_amount
            print(f"{withdraw_amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
