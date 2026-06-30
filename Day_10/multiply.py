
# This program takes a number as input and prints its multiplication table from 1 to 10.
number = int(input("Enter a number: "))

for i in range (1,11):
    result = number * i
    print(f"{number} x {i} = {result}")


# This program takes a number as input and calculates the sum of that number added to each integer from 1 to 10.
total = 0
for i in range(1, 11):
    total = total + i

print("Sum = ", total)