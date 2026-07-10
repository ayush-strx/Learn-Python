#Data structures are used for storing and organizing data in a way that allows for efficient access and modification. Common data structures include lists, tuples, sets, dictionaries, and more complex structures like stacks, queues, linked lists, trees, and graphs. Each data structure has its own strengths and weaknesses, making them suitable for different types of applications.

# But we only focus on the most commonly used data structures in Python: lists, tuples, sets, and dictionaries.

#------------------------------------------------------------------------
#1. List (list): Used to store multiple items in a single variable. Ordered and changeable.
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Lists methods: there are many methods available for lists in Python, some of the most commonly used ones are:

 # append(): Adds an item to the end of the list.
 #example:
vegetables = ["carrot", "potato"]
vegetables.append("tomato")  # Adds "tomato" to the end of the list
print(vegetables)  # Output: ['carrot', 'potato', 'tomato']

# insert(): Adds an item at a specified index.
# remove(): Removes the first item with the specified value.
# pop(): Removes the item at the specified index (or the last item if index is not specified).
#sort(): Sorts the list in ascending order.
#reverse(): Reverses the order of the list.

#------------------------------------------------------------------------

#2. Tuple (tuple): Similar to lists but cannot be changed after creation. Ordered and unchangeable.
coordinates = (10, 20)  
print(coordinates)

# Tuple methods: there are only two methods available for tuples in Python:
# count(): Returns the number of times a specified value appears in the tuple.
#example:
my_tuple = (1, 2, 3, 1, 4)
print(my_tuple.count(1))  # Output: 2

# index(): Returns the index of the first occurrence of a specified value.
#example:
print(my_tuple.index(3))  # Output: 2

#-------------------------------------------------------------------------

#3. Set (set): Used to store unique items. Unordered and unindexed.
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)

# Set methods: there are many methods available for sets in Python, some of the most commonly used ones are:
# add(): Adds an item to the set.
#example: 
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}

# remove(): Removes the specified item from the set.
# union(): Returns a set that contains all items from both sets.
# intersection(): Returns a set that contains only the items that are present in both sets.

#--------------------------------------------------------------------------

#4. Dictionary (dict): Used to store data in key-value pairs.
person = {"name": "Ayush", "age": 19}
print(person)                               

# Dictionary methods: there are many methods available for dictionaries in Python, some of the most commonly used ones are:
# keys(): Returns a list of all the keys in the dictionary.
#example:
student = {"name": "Ayush", "age": 19, "grade": "A"}
print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])

# values(): Returns a list of all the values in the dictionary.
# items(): Returns a list of all the key-value pairs in the dictionary.
# get(): Returns the value for a specified key.