marks = int(input("Please enter your marks: "))

if (marks<50):
    print("You have failed.")
elif (marks<60):
    print("You have passed with a D grade.")
elif (marks<70):
    print("You have passed with a C grade.")
elif (marks<80):
    print("You have passed with a B grade.")
else:
    print("You have passed with an A grade.")