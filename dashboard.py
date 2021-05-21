from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title('image')
root.iconbitmap('C:/Users/INTEL/PycharmProjects/pythonProject1/pics/tk1.3.ico')#u need to write the location in here
#root.geometry ("1920x1080")
#define image
bg=ImageTk.PhotoImage(file='C:/Users/INTEL/PycharmProjects/pythonProject1/iig security/img_buttons/user 5.png')

img1=PhotoImage(file='C:/Users/INTEL/PycharmProjects/pythonProject1/iig security/img_buttons/user 4.png')
img2=PhotoImage(file='C:/Users/INTEL/PycharmProjects/pythonProject1/iig security/img_buttons/rc1.png')




my_canvas= Canvas (root,width=1920,height=1080)
my_canvas.pack(fill='both',expand=True)

#set image in canvas
my_canvas.create_image(0,0, image=bg,anchor='nw')



button1=Button(root,image=img1,borderwidth=0,)
B2=my_canvas.create_window(70,70,anchor='nw',window=button1)

button2=Button(root,image=img2,borderwidth=0,)
B2=my_canvas.create_window(250,70,anchor='nw',window=button2)


root.state('zoomed')#to do full screen

root.mainloop()