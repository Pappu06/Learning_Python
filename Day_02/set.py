# Sets in python (unordered, mutable, no duplicates)

numbers = {1, 2, 3, 4, 5}
print(numbers)

# add items
numbers.add(6)
numbers.add(3)  # duplicate, will not be added
print(numbers)

# remove items
numbers.remove(2)
print(numbers)

# check if item exists
print(3 in numbers)