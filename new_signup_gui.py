from tkinter import *
from tkinter import messagebox
import signup_class

root = Tk()
root.title("Sign-Up")

uname_tbox = Entry(root, bg="yellow", fg="magenta")
pass_tbox = Entry(root, bg="yellow", fg="magenta")

uname_tbox.grid(row=0, column=1, columnspan=10)
pass_tbox.grid(row=1, column=1, columnspan=10)

uname_label = Label(root, text="Username", font=('calibre', 10))
uname_label.grid(row=0, column=0)

pass_label = Label(root, text="Password", font=('calibre', 10))
pass_label.grid(row=1, column=0)


def taken_in_credentials():
    userid = uname_tbox.get()
    password = pass_tbox.get()
    # length_of_password = len(password)

    obj = signup_class.Signup()
    repeat_username = obj.check_username_repeatation(userid)
    password_stop = obj.check_password(password)[0]
    password_weak = obj.check_password(password)[1]

    if repeat_username is False and password_stop is False:
        if password_weak:
            messagebox.showwarning("Warning", "Password is weak . Doesn't contain any special character.")
        else:
            obj.store_username_passid(userid, password)
            messagebox.showinfo("Information", "Credentials added successfully")
            button['state'] = DISABLED

    if repeat_username:
        # username_output = Label(root, text="Username already present. Please enter a new username.", fg='red')
        messagebox.showerror("Error", "Username already in use! Enter a new username .")

    if password_stop:
        messagebox.showerror("Error", "Password length less than 5. Please add a longer password.")




text_shown = Text(root, height=5, width=15, bg="light cyan", fg="magenta")
text_shown.grid(row=3, column=1)

button = Button(root, text="Submit", command=lambda: taken_in_credentials())
button.grid(row=2, column=1)

root.mainloop()
