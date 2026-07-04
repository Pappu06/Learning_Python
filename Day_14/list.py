fruits = ["apple", "banana", "cherry"]

# update list
fruits[1] = "blueberry"

# Adding an item to the end of the list
fruits.append("orange")
fruits.append("grape")
fruits.append("mango")
fruits.append("pineapple")

# Inserting an item at a specific index
fruits.insert(1, "kiwi")

# Removing an item from the list
fruits.remove("cherry")

# Removing an item by index using pop()
fruits.pop(2)


print(len(fruits))
print(fruits)

# Loop through the list
for fruit in fruits:
    print(fruit)