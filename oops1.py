# initiate a class
class employee:
    # special func/magic method, dunder method
    # There're a lot special method, to define data/attribute which dunder method we are using its called constructor.
    def __init__(self):  # constructor to construct and initiate all required dependecies automatically that is reuired application to run or set default properties or data, which we are not expecting from user to do these things manually. 
        # These __init__ constructor help us precisely to make attributes.
        # This is not the only special method.
        # You can search in browser 'Dunder or magic methods in python'
        # print("Started executing attributes/data")
        print(id(self))  # o/p- 140116878211216
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("attributes/data have been initiated")
    
    # def travel(self, destination):
    # def travel(destination):   # TypeError: employee.travel() takes 1 positional argument but 2 were given
        # This means when you use method by using object, bydefault the object comes as bydefault parameter inside parenthesis() and you no need to pass explicitely.
        # since, as this comes automatically, due to this reason during making a class inside constructor, attributes, everywhere we are using self.
        # if employee object is sam then, all above are sam constructor/ sam data/attributes & the method which can be accessible by sam.
        # Object itself is 'self'.
    def travel(destination):
        print("This travel method was called manually")
        # print(f"Employee is now travelling to {destination}")
        print(f"Employee is now travelling to Delhi")
# create an obj/instance of the class
sam = employee()
# sam.name = "Sam Kumar"  # You can create attribute and access it outside class as well, as per software functionality need.
# print(id(sam))  # o/p- 140116878211216, which is same as self id. This means self is object itself. 
# print(sam.name)

# shaktiman = employee()
# print(id(shaktiman))

# printing the attributes
# print(sam.id)

# calling a method
# sam.travel("Goa")
# sam.travel()

# print(type(sam))


