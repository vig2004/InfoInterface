from tkinter import *
from time import strftime
import signin_class

# creating tkinter window
root = Tk()
root.title('Login')
root.geometry('320x205')#Don't change the geometry.

intro_root = Label(root,text="Welcome back to IIG, User ! \n", font = ('calibre', 10, 'bold'), fg="Magenta")#Rahul you may give any colour you like and anyone can change the text if you want.
intro_root.grid(row=0,column=1)

username_box = Entry(root, width=50, borderwidth=5, bg="cyan", fg="purple")#Rahul you may give any colour you like
username_box.grid(row=1, column=0, columnspan=3)
username_box.insert(0,"Enter your username.")

password_box = Entry(root, width=50, borderwidth=5, bg="cyan", fg="purple")#Rahul you may give any colour you like
password_box.grid(row=2, column=1, columnspan=3)
password_box.insert(0, "Enter your password")


def check_username_password():
    userid = username_box.get()
    passid = password_box.get()
    #label=Label(root,width=35,text=(userid,passid),fg="magenta")
    #label.grid(row=3,column=1)
    obj=signin_class.log()
    chck=obj.signin(userid,passid)

    if chck[0] == False :
        password_box.delete(0,END)
        global count
        count_no_loops =1

        text_error_shown.insert(END, "Incorret Password . ")

        while count_no_loops < 4:
            root.after(20000,check_username_password)
            if chck[0] == True :
                button['state'] == DISABLED
                break
            count_no_loops+=1

    if chck[1] == False:
        username_box.delete(0, END)
        text_error_shown.insert(END, "Wrong Username entered . ")

    if chck[0] == True and chck[1] == True:
        text_error_shown.insert(END,"Successful Authentication . ")
        button['state'] = DISABLED

        if chck[2] == True :
            text_error_shown.insert(END,"Hello Admin .")

text_error_shown = Text(root, height=3, width=38, bg="light cyan")#Rahul you must not  give any colour you like #Hehe
text_error_shown.grid(row=6,column=1)

space_given = Label(root,text="")
space_given.grid(row=4 ,column=1)

button = Button(root, padx=25, pady=5, text="Submit", command=check_username_password)
button.grid(row=3, column=1, columnspan=2)

root.resizable(True, True)
root.mainloop()

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

from tkinter import *
import signup_class

root = Tk()
root.title("Sign-Up")

username_entry_box = Entry(root, bg="yellow", fg="magenta")
password_entry_box = Entry(root, bg="yellow", fg="magenta")

username_entry_box.grid(row=0, column=1, columnspan=10)
password_entry_box.grid(row=1, column=1, columnspan=10)

username_label = Label(root, text="Username", font=('calibre', 10))
username_label.grid(row=0, column=0)

password_label = Label(root, text="Password", font=('calibre', 10))
password_label.grid(row=1, column=0)


def taken_in_credentials():
    userid = username_entry_box.get()
    password = password_entry_box.get()
    # length_of_password = len(password)

    obj = signup_class.signup()
    repeat_username = obj.check_username_repeatation(userid)
    password_stop = obj.check_password_length(password)

    if repeat_username is False and password_stop is False:
        obj.store_username_passid(userid, password)
        text_shown.insert(END, " Username and Password added Successfully!")
    if repeat_username:
        # username_output = Label(root, text="Username already present. Please enter a new username.", fg='red')
        text_shown.insert(END, "Username already present. Please enter a new username")

    if password_stop:
        text_shown.insert(END, "Password length less than 5. Enter a bigger password")


text_shown = Text(root, height=5, width=30, bg="light cyan", fg="magenta")
text_shown.grid(row=3, column=1)

button = Button(root, text="Submit", command=lambda: taken_in_credentials())
button.grid(row=2, column=1)

root.mainloop()

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