# Creating a dictionary
my_dict = {
    "name": "Asif",
    "age": 25,
    "profession": "Engineer"
}

# Accessing values by keys
print("Name:", my_dict["name"])  # Output: Asif

# Adding or modifying key-value pairs
my_dict["age"] = 26
my_dict["city"] = "Dhaka"
print("Updated dictionary:", my_dict)  # Output: {'name': 'Asif', 'age': 26, 'profession': 'Engineer', 'city': 'Dhaka'}

# Removing a key-value pair
my_dict.pop("profession")
print("After removing 'profession':", my_dict)  # Output: {'name': 'Asif', 'age': 26, 'city': 'Dhaka'}

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, ":", value)
