# Assignment: Python Data Structures

# Task 1: Working with Lists
list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original List: {list}")
list.append('mango')
print(f"Appended List: {list}")
list.remove('banana')
print(f"List after removal: {list}")
list.reverse()
print(f"Reversed List: {list}")

# Task 2: Exploring Dictionaries 
my_dict = {"name":"Kimone", "age": 22, "city":"Halifax"}
my_dict.update({"favorite color":"Purple"})

my_dict.update({"city":"Toroto"})

print(my_dict)

print("Keys: ",", ".join(my_dict.keys()))
print("Values: ",", ".join(map(str, my_dict.values())))

# Task 3: Using Tuples

