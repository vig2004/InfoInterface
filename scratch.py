'''from tkinter import *
root = Tk()
COUNT = 1

def task():
    inner_root = Tk()
    inner_root.title("Inner Root")

def f2():
    print("World")

root.after(2000, task)
button=Button(root,text="Click",command=task() and f2)
button.pack()

root.mainloop()'''

