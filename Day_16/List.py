my_array  = [10, 20, 30, 4, 50, 60, 70, 80, 90, 100]

min_value = my_array[0]

for x in my_array:
    if x < min_value:
        min_value = x

print("The minimum value in the array is:", min_value)