# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 155

# print(type(lst))
# print(type(my_str))
# lst.clear()
# print(lst)

# my_str = my_str.capitalize()
# print(my_str)

# In python, everything including data structure, data types all are belongs from class developed by devs.
# Thats why python called as OOPS. Everything in python is an Object.

# a = 'x'
# b = 'y'
# print(a+b)
# o/p- xy
# its bcos in python doesn't have algebra till now didn't create
# you can create such datatype (Algebra) by the help oops concept you can use such magic methods, to get an o/p for algebra in this format. O/p (x+y)
# you can use '__add__' method.
# Not necessarily to remember every dunder method, but just to give insight there'r alot dunder method, if there's need then you can use.


# This is called modular coding.
from oops_proj import chatbook

# static method. 
# To access a static variabel / static method within the class "chatbook.__user_id", instead of self this is accessible from class directly.
user1 = chatbook()
print(user1.id)

# chatbook.set_id(10)
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)


# user1 = chatbook()
# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

# o/p- 0
#      1
#      2

# This is called static method.


# user1 = chatbook()
# print(user1.user_id)

# user2 = chatbook()
# print(user2.user_id)

# user3 = chatbook()
# print(user3.user_id)

# o/p- 1
#      1
#      1


# getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

# o/p - Default User
#       Agent X



# print(user1.__name)  # o/p- AttributeError: 'chatbook' object has no attribute '__name'
# suppose you make a class called employee and you create an id attribute. this stored in memory simply as id.
# which you can access it bydefault format (obj.id) and can print it.

# lets do it
# print(user1._chatbook__name) # "objname._classname__attribute/methodname"
# you can't fully protect in Python. 

# But When you add '__' infront of attribute, then it save in memory as "_classname__attribute/methodname" and you can access it by adding objname. just like "objname._classname__attribute/methodname".


# function vs method below
# lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

# # method- However if we call a method, then we have to keep object first.
# user1 = chatbook()
# user1.sendmsg()

# Note: To use function, we are directly called a function as we see in above example, and when we calling inbuilt function by putting dot '.' after the object then this called as method.
# This is difference b/w method and function. Methos is also a function which is written under a class.
# Just like, when we create as object of pandas by importing it as pd. those are actually functions written in pandas class.

# In your project if you have a need to create a way, so that user from outside can access the hidden attribute and change it too.
# getter and setter --> to get the hidden attribute and to set the hidden attribute.

