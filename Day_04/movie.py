movie = ['Deadpool', 'Inception', 'Interstellar']
print(movie)

# access the first element and last element

print(movie[0]) # access the first element
print(movie[-1]) # access the last element

# add an element to the end of the list and first of the list

movie.append('Avatar') # add an element to the end of the list
movie.insert(0, 'The Dark Knight') # add an element to the start of the list
movie.insert(2, 'The Matrix') # add an element to the 2nd index of the list
print(movie)

# remove an element from the list
movie.remove('Inception') # remove an element from the list
movie.pop(2) # remove the last element from the list
print(movie)

# iterate through the list
for i in movie:
    print(i)