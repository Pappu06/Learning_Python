numbers = [5, 10, 15, 20, 25, 30]

# All even numbers.
for num in numbers:
    if num % 2 == 0:
        print(num)

# The sum of all odd numbers.
sum_odd = 0
for num in numbers:
    if num % 2 != 0:
        sum_odd += num
print("Sum of odd numbers:", sum_odd)

# The average of all numbers.
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average of all numbers:", average)

# The second largest number (without using sort() or max()).
# largest = numbers[0]
# second_largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
# print("Second largest number:", second_largest)

numbers = [5, 10, 15, 20, 25, 30]

if len(numbers) < 2:
    print("No second largest number.")
else:
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    print("Largest:", largest)
    print("Second largest:", second_largest)
