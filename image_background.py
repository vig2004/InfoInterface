from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title('image')
root.iconbitmap('img/tk1.3.ico')#u need to write the location in here
root.geometry ("1920x1080")
#define image
bg=ImageTk.PhotoImage(file='img/bl11.png ')


def open():
    root.destroy()

    import gui_signup

def open1():
    root.destroy()

    import gui_signin

img1=ImageTk.PhotoImage(file='img/su11.png ')
img2=ImageTk.PhotoImage(file='img/si11.png ')

my_canvas= Canvas (root,width=1920,height=1080)
my_canvas.pack(fill='both',expand=True)

#set image in canvas
my_canvas.create_image(0,0, image=bg,anchor='nw')

               #horizontal #vertical


my_canvas.create_text(950,650,text='Please sign up or sign in to continue',font=('Algerian', 25),fill='black')


button1=Button(root,image=img1,borderwidth=0,command=open)
button2=Button(root,image=img2,borderwidth=0,command=open1)


B1=my_canvas.create_window(390,700,anchor='nw',window=button1)
B2=my_canvas.create_window(1050,700,anchor='nw',window=button2)



#to do full screen

root.mainloop()