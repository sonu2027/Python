# 1. Defining a Class:
# A class contains methods (functions) and attributes (variables) that define its behavior and state.

class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
# 2. Creating an Object (Instance):
person1 = Person("Alice", 25)
person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.

# 3. The __init__ Method:
# The __init__ method is a special method that gets called when you create an object. It's used for initializing the object's attributes.