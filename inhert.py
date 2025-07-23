# Simple inheritance

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # # # Derived class
# class Dog(Animal):
#     def __init__(self):
#         self.behaviour = "friendly"

#     def speak(self):
#         print(f"{self.name} barks. He is very {self.behaviour}")
#         # you you have no constructor in child class, then bydefault python enter to the parent class, and treat parent class attribute to as child class.
#         # But if you initiate attribute with the hel of constructor inside child class, then parent class attributes are gets not-inherited.
#         # This is called constructor overloading. By making constructor in child class and python avoid parent class constructor.
#         # Method overloading also we have learnt, if already same parent class method name exist in child class, rather than using the method of parent class, it used own method of child class.

# # # # Create an instance of Animal
# # animal = Animal("Generic Animal")
# # animal.speak()  # Output: Generic Animal makes a sound.

# # # # Create an instance of Dog
# dog = Dog()
# dog.speak()  # Output: Buddy barks.



# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()  # To resolve constructor overloading issues/To inherit method from parent class constructor's attributes.
        # if you want to keep parent class constructor's attributes and additionally also want to define attributes in child class.
        # In this case use super() keyword.
        self.breed = breed

    def speak(self):
        super().speak()  # Again we use super() keyword and the method .speak() which we want to inherit from the base class/parent class method.
        # This will print in o/p as Buddy makes a sound.
        print(f"{self.name} barks. It is a {self.breed}.")
        # o/p - Buddy barks. It is a Golden Retriever.

        # Note: If you have logic in child class, so that with same method name you want to call from parent class as well as child class
        # then, call parent class method from child by using, 'super().speak()'
        # then after you can access the same name in child class, which you have already used in parent class. 'print(f"{self.name} barks. It is a {self.breed}.")'


# # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.
# Buddy barks. It is a Golden Retriever.

# Note: you can't access super() outside child class. Such as with child class object from outside. can't accessible.
# super() help us to inherit methods, both construct(special method) and other normal method.
# Cant access individually any attribute from parent class.


# something like,
# dog.super().speak()
# o/p- AttributeError: 'Dog' object has no attribute 'super'