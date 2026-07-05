numbers = [12, 25, 37, 48, 59, 63, 71, 84]

#first four numbers
print(numbers[0:4])

#last three numbers
print(numbers[-3:])

# print odd numbers
for i in numbers:
    if i % 2 != 0:
        print(i)

#reverse the list
print(numbers[::-1])