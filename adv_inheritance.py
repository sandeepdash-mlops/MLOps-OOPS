# Single or Basic Inheritance

# Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Alice")
# child.greet()  # Output: Hello, my name is Alice.
# child.play()   # Output: Alice is playing.

# ------------------------------------------------------------

# Multilevel Inheritance

# Base class
# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # Intermediate class
# class Parent(Grandparent):

#     def work(self):
#         print(f"{self.name} is working.")

# # Derived class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Charlie")
# child.tell_story()  # Output: Charlie tells a story.
# child.work()        # Output: Charlie is working.
# child.play()        # Output: Charlie is playing.

# ------------------------------------------------------------

# Hierarchical Inheritance

# Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class 1
# class Child1(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Derived class 2
# class Child2(Parent):

#     def study(self):
#         print(f"{self.name} is studying.")

# # Create instances of Child1 and Child2
# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()  # Output: Hello, my name is Dave.
# child1.play()   # Output: Dave is playing.

# child2.greet()  # Output: Hello, my name is Eve.
# child2.study()  # Output: Eve is studying.

# ------------------------------------------------------------

# Multiple Inheritance (Diamond Problem)

# Common base class
# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# # Intermediate class 1
# class B(A):

#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# # Intermediate class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()

# # Derived class
# class D(B, C):

#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# # Create an instance of D
# d = D("Frank")
# d.greet() 

# # Output:
# # Hello from D, Frank.
# # Hello from B, Frank.
# # Hello from C, Frank.
# # Hello from A, Frank.

# Note:
# As both B and C inherit from A and both calling super() A greet method, but still super() calls A.greet() only once as Python is smart: it avoids calling the same method multiple times
# Because Python uses the C3 linearization algorithm to determine the order in which classes are resolved. This ensures:

# super() follows the MRO, not the parent class directly.
# means When you use super(), Python doesn’t just go to the parent class. Instead, it goes to the next class in the Method Resolution Order (MRO) — a special order Python calculates based on inheritance.
# When you use super() in Python in a class that is part of a multiple inheritance hierarchy, it does NOT call the parent class directly.

# Instead: super() looks at the next class in the MRO list, not the parent in the code.
# Python ensures each class's method in the hierarchy is called only once.
# This avoids duplication and infinite loops in diamond inheritance.
# Now, if you print:
# print(D.__mro__)
# O/p- (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# So even though B inherits from A,
# The super() in B goes to C because Python is not following the inheritance tree directly (here, Not on direct parent) — it's following the MRO linear chain.
# That’s why we say:
# "super() doesn’t mean ‘go to parent’ — it means ‘go to next in MRO.’". B inherits from A	Yes, directly But super() in B goes to C based on the next class in the Method Resolution Order (MRO)

# ------------------------------------------------------------

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# # Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# # Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# # Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# # Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.

# "If a child class (like Bat) has its own constructor, then it must use super() to access the parent’s constructor."
# Yes — but only applies to constructors (__init__), not to methods like fly() or feed().

# You can access all methods of parent classes just by inheriting from them — no need to call super() or even call the parent constructor unless their methods depend on something initialized in it.
# means, If a method in the parent class needs some data or attribute (like self.name) that is only created inside the parent's constructor (__init__),
# then you must call the parent's constructor (via super() or directly), otherwise that method will crash.

# Example code:
# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hi, I am {self.name}")

# class Child(Parent):
#     def __init__(self):
#         print("Child init — but not calling super().__init__")

# c = Child()
# c.greet()  # Error: AttributeError: 'Child' object has no attribute 'name'

# Solution:

# Fix it with super()

# class Child(Parent):
#     def __init__(self):
#         super().__init__("Bruce")  # Calls parent's constructor

# c = Child()
# c.greet() 

# ------------------------------------------------------------