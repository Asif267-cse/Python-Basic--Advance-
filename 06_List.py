# Creating a list
my_list = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", my_list[0])  # Output: 10

# Modifying elements
my_list[2] = 35
print("Modified list:", my_list)  # Output: [10, 20, 35, 40, 50]

# Adding elements
my_list.append(60)
print("After appending 60:", my_list)  # Output: [10, 20, 35, 40, 50, 60]

# Removing elements
my_list.remove(20)
print("After removing 20:", my_list)  # Output: [10, 35, 40, 50, 60]

# Slicing (getting a sublist)
print("Sliced list [1:3]:", my_list[1:3])  # Output: [35, 40]

# Iterating over the list
for item in my_list:
    print(item)
