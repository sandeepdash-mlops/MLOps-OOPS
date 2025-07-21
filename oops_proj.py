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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        # else if the user is pressing any other key then,
        else: 
            exit()
    # Main menu work is done.


obj = chatbook()
        
    