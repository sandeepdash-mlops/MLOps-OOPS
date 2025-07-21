# initiate a class
class employee:
    # special func/magic method, dunder method
    # There're a lot special method, to define data/attribute which dunder method we are using its called constructor.
    def __init__(self):  # constructor to construct and initiate all required dependecies automatically that is reuired application to run or set default properties or data, which we are not expecting from user to do these things manually. 
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")
    
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")
# create an obj/instance of the class
sam = employee()

# printing the attributes
# print(sam.id)

# calling a method
# sam.travel("Goa")

print(type(sam))