# Assignment: Python Data Structures

# Task 1: Working with Lists
# Create a new list
list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original List: {list}")

# Update a list
list.append('mango')
print(f"Appended List: {list}")

# Remove an item from the list
list.remove('banana')
print(f"List after removal: {list}")

# Reverse the list
list.reverse()
print(f"Reversed List: {list}")

# Task 2: Exploring Dictionaries 

# Create a dictionary 
my_dict = {"name":"Kimone", "age": 22, "city":"Halifax"}

# Add and update the dictionary
my_dict.update({"favorite color":"Purple"})
my_dict.update({"city":"Toroto"})

print(my_dict)

# Prints the keys and values 
print("Keys: ",", ".join(my_dict.keys()))
print("Values: ",", ".join(map(str, my_dict.values())))

# Task 3: Using Tuples

# Create a new tuple
fav_things = ('Maze Runner', 'Luther', 'The Silent Patient')

# Prints the tuple
print(fav_things)

# Tries to update the tuple but gets an error
# fav_things[1]= 'Be Humble'

# Prints the length of the tuple
print(len(fav_things))