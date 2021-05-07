class signup :

    def check_username_repeatation(self, userid):
        self.username = userid
        username_repetation = True

        with open("username.txt", "r+") as f:
            ar = f.readlines()
        user_ar = []
        #for username array
        for i in ar:
            user_ar.append(i.replace('\n', ""))

        if self.username.endswith("@IIG"):
            boolean_username = (self.username) in user_ar
        else :
            boolean_username = (self.username+"@IIG") in user_ar

        if boolean_username is True :
            username_repetation = True
        else :
            username_repetation = False

        return username_repetation

    def check_password_length(self, password):
        self.passid = password
        len_pass = len(self.passid)
        stop = True
        if len_pass < 5 :
            stop = True
        else :
            stop =False
        return stop

    def store_username_passid(self,userid, password):
        self.userid = userid
        task1 = open("Username.txt", "a+")  # Enters the new username in Username.txt
        task1.write("\n")

        if (self.userid).endswith("@IIG") : #Adds @IIG behind the userid if @IIG not present
            task1.write(self.userid)
            task1.close()
        else :
            task1.write(self.userid+"@IIG")
            task1.close()
        #print("Added")

        self.passid = password
        task2 = open("Passwords.txt", "a+")  # Enters the new username in Username.txt
        task2.write("\n")
        task2.write(self.passid)


'''obj = trial_signup()
result=obj.check_username("Rahul@IIG")
print(result)'''