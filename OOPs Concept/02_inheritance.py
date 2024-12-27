# 1. Inheriting from a Parent Class:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inherits from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.speak()  # Output: Buddy barks.

# 2. Using super() to Access Parent Class Methods:
# The super() function allows you to call methods from the parent class.

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the __init__ method of Animal class
        self.breed = breed
        
# 3. Overriding Methods:
# The child class can override methods from the parent class.