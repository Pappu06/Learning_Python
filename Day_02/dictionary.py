# Dictionary in python (unordered, mutable, no duplicates)

person = {
    "name": "Pappu", 
    "age": 23, 
    "city": "Ranchi"
    }
print(person)

# access items
print(person["name"])  # access by key
print(person.get("age"))  # access by get method

# add items
person["email"] = "xyz123@gmail.com"
print(person)   