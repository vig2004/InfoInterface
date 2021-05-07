from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title('image')
root.iconbitmap('C:/Users/INTEL/PycharmProjects/pythonProject1/pics/tk1.3.ico')#u need to write the location in here
#root.geometry ("1920x1080")
#define image
bg=ImageTk.PhotoImage(file='C:/Users/INTEL/PycharmProjects/pythonProject1/pics/img/bg1.png ')


def open():
    root.destroy()

    import gui_signup

def open1():
    root.destroy()

    import gui_signin




my_canvas= Canvas (root,width=1920,height=1080)
my_canvas.pack(fill='both',expand=True)

#set image in canvas
my_canvas.create_image(0,0, image=bg,anchor='nw')

               #horizontal #vertical
my_canvas.create_text(950,100,text='IIG',font=('Algerian', 100),fill='black')#fill to change color of the font in canvas

my_canvas.create_text(950,200,text='(INFO FOR GAMERS)',font=('Algerian', 50),fill='black')

my_canvas.create_text(950,650,text='Please sign up or sign in to continue',font=('Algerian', 30),fill='black')


button1=Button(root,text='SIGN UP',font=('Algerian', 30),command=open)
button2=Button(root,text='SIGN IN',font=('Algerian', 30),command=open1)


B1=my_canvas.create_window(650,700,anchor='nw',window=button1)
B2=my_canvas.create_window(1050,700,anchor='nw',window=button2)



root.state('zoomed')#to do full screen

root.mainloop()