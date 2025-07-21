class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        # As we know already when object is ready constructor called by itself.
        # During object creation, i want to show meny to my users, like what to do after this platform, decide it.
        self.menu()

    def menu(self):
        user_input = input("""welcom to chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        
        if user_input == "1":
            # pass
            self.signup()
        elif user_input == "2":
            # pass
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
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
    

obj = chatbook()
        
    