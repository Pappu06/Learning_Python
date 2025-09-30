# lists in python are mutable, ordered sequences of elements    

fruits = ['apple', 'banana', 'cherry']
print(fruits)  # access the first element
fruits.append('orange')  # add an element to the end of the list
fruits.remove('banana')  # remove an element from the list
print(fruits)  

for i in fruits:  # iterate through the list
    print(i)