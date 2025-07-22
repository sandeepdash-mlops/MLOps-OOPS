class chatbook:

    __user_id = 1
    def __init__(self):
        # This is how you access a static variabel / static method within the class, instead of self this is accessible by class directly.
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User" # encapsulation means hiding the attributes and make it hidden attribute with '__', which you wouldn't want to access this by others.

        # static method
        # self.user_id = 0
        # as long as you create an object and during constructor call we make it '+= 1'
        # self.user_id += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # As we know already when object is ready constructor called by itself.
        # During object creation, i want to show meny to my users, like what to do after this platform, decide it.
        # self.menu()


    # __user_id = 1
    # lets implement gett and setter for this, also lets clear how to make static method.

    @staticmethod    # this is staticmethod flag as decorator, to tell outside user that it's a static method, and you'll understand how it different from other methods.
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):   # dont use self here, as to access static method there is no need of object to access staticmethod, as its been called directly from class
        chatbook.__user_id = val

    # getter -> can be anyname, it's not a keyword
    def get_name(self):
        return self.__name # can be access hidden attribute within class using normal way obj.attribute name. no need to define "objname._classname__attribute/methodname" justlike to access it from outside.
    

    # setter -> can be anyname, it's not a keyword
    def set_name(self, value): # value is a new name which you want to set.
        self.__name = value

    def menu(self):
        user_input = input("""welcom to chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        
        if user_input == "1":
            # pass
            self.signup()
        elif user_input == "2":
            # pass
            self.signin()
        elif user_input == "3":
            # pass
            self.my_post()
        elif user_input == "4":
            # pass
            self.sendmsg()
        # else if the user is pressing any other key then,
        else: 
            exit()
    # Main menu work is done.


    # Now to define individual methods for menu list
    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("create your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("enter your passwd here -> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input correct creds..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here ->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something..")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter message ->")
            frnd = input("whom to send the msg? ->")
            print("Your message has been sent to {frnd}")
        else:
            print("You need to sign in first to message..")
        print("\n")
        self.menu()
    

# user1 = chatbook()
        
    