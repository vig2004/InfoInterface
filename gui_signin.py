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
