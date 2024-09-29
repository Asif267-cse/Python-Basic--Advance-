# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])  # Output: 1

# Tuples are immutable, so elements can't be changed
# my_tuple[1] = 20  # This will raise an error

# Slicing (getting a subtuple)
print("Sliced tuple [1:4]:", my_tuple[1:4])  # Output: (2, 3, 4)

# Iterating over the tuple
for item in my_tuple:
    print(item)
