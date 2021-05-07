class log:

    def signin(self,userid,passid):
        # Final Class
        #for username array
        signin = False
        authorisation =False
        admin = False
        with open("username.txt", "r+") as f:
            ar = f.readlines()
        user_ar = []
        #for password array
        for i in ar:
            user_ar.append(i.replace('\n', ""))
        with open("Passwords.txt", "r+") as file:
            pas = file.readlines()
            pass_ar = []
            for i in pas:
                pass_ar.append(i.replace('\n', ""))
        #for aadmin check
        with open("Admin.txt", "r+") as f:
            ar = f.readlines()
        admin_ar = []
        for i in ar:
            admin_ar.append(i.replace('\n', ""))

        login = dict(zip(user_ar, pass_ar))
        self.username = userid
        self.password = passid

        if self.username in login:  # Checks whether username and password given by user match
            authorisation=True

            if self.username in admin_ar:
                admin = True

            if login[self.username] == self.password:
                 #print("Succesful Authentication")
                 signin=True

            else:
                pass
        else :
            #print("Wrong username.")
            signup=False

        list1=[signin,authorisation,admin]
        return list1

