# Key-value pairs for mapping data.

student = {"name": "Alice", "age": 21, "grade": "A"}

# Accessing Values
print(student["name"])  # Alice

# Modifying Value
student["name"] = "sonu"

# Adding Values
student["subject"] = "Math"
print(student)  # {'name': 'Alice', 'age': 21, 'grade': 'A', 'subject': 'Math'}

# Removing Key-Value Pairs:
del student["age"]

# Dictionary Methods:
# keys() – Returns all the keys.
# values() – Returns all the values.
# items() – Returns all the key-value pairs.
# get() – Accesses the value of a key, returns None if the key doesn’t exist.
