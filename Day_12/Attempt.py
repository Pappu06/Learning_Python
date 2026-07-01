# for i in range(1,11):
#     if i == 6:
#       break

#     print(i)

correct_password = "python123"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break

    print("Access denied. Try again.")