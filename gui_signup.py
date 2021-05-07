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
