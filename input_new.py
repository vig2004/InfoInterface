from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox


root = Tk()
processor_name_entry = Entry(root, width=30, borderwidth=6)
processor_frequency_entry = Entry(root, width=30, borderwidth=6)
ram_entry = Entry(root, width=30, borderwidth=6)
storage_type = Entry(root, width=30, borderwidth=6)
ques = Entry(root, width=30, borderwidth=6)

mylabel = Label(root, text="Processor Name:")
mylabel1 = Label(root, text="base speed of processor")
mylabel2 = Label(root, text="Enter RAM(in GB)")
mylabel5 = Label(root, text="Enter the type of storage (SSD/HDD)")
queslabel = Label(root, text="Ext graphic card in your PC (Y/N)")
vram = 0
gpu = ""
storage_meth = ""
pro_freq = 0
pro_name = ""
ram = 0


def afterQuestion():
    opt = ques.get()
    if opt == "y" or opt == "Y":
        top = Toplevel()
        top.title("2nd scrn")
        info_label1 = Label(top, text="This scrn consists of the rest of the entry fields")
        info_label1.grid(row=0, column=0)
        gpu_name = Entry(top, width=30, borderwidth=6)

        vram_entry = Entry(top, width=30, borderwidth=6)

        #storage_type = Entry(top, width=30, borderwidth=6)

        mylabel3 = Label(top, text="Enter ur GPU's full name")
        myLabel4 = Label(top, text="Enter the VRAM your GPU has :")
        #mylabel5 = Label(top, text="Enter the type of storage (SSD/HDD)")
        vram_entry.grid(row=2, column=1)
        gpu_name.grid(row=1, column=1)
        # storage_type.grid(row=3, column=1)
        mylabel3.grid(row=1, column=0)
        myLabel4.grid(row=2, column=0)
        # mylabel5.grid(row=3, column=0)

        def data():
            pro_name = processor_name_entry.get()
            pro_freq = processor_frequency_entry.get()
            ram = ram_entry.get()
            vram = vram_entry.get()
            gpu = gpu_name.get()
            storage_meth = storage_type.get()
            mydb = mysql.connect(host='localhost', user='root', passwd='Ghan@20$',
                                 database='iig')  # guys use your own password.
            cursor = mydb.cursor()
            # cursor.execute("create table iig_inputs(processor_name varchar(45),processor_frequency float,ram int,vram int,gpu varchar(45),storage_type varchar(3))")
            # while running for first time de-comment to the above line. After first use re-comment it.
            if pro_name == "" or str(pro_freq) == "" or str(ram) == "" or str(vram) == "" or gpu == "" or storage_meth == "":
                messagebox.showwarning("Warning.", "Please fill in empty entries/entry!")

            else:
                query = ("insert into iig_inputs(processor_name, processor_frequency, ram, vram, gpu, storage_type) values (%s, %s, %s, %s, %s, %s)")
                values = (pro_name, pro_freq, ram, vram, gpu, storage_meth)
                cursor.execute(query, values)
                mydb.commit()
                messagebox.showinfo("Success", "Credentials entered successfully!")
                root.destroy()
                #top.destroy()
                import Games_Teir
            mydb.close()

        button = Button(top, text="Submit", command=data)
        button.grid(row=4, column=1, columnspan=2)
        top.mainloop()

    elif opt == "n" or opt == "N":
        messagebox.showwarning("Warning!!!!!", " do you  want to continue without an external gpu?!(Y/N)")
        top1 = Toplevel()
        top1.title("3rd scrn")
        Ques2 = Label(top1, text="Do u want to continue without an external gpu(Y/N)")
        Q2 = Entry(top1, width=30, borderwidth=7)

        Q2.grid(row=0, column=1)
        Ques2.grid(row=0, column=0)
        opt2 = ""
        def new_window():
            opt2 = Q2.get()
            pro_name = processor_name_entry.get()
            pro_freq = processor_frequency_entry.get()
            ram = ram_entry.get()
            storage_meth = storage_type.get()
            if pro_name == "" or str(pro_freq) == "" or str(ram) == "" or storage_meth == "":
                messagebox.showwarning("Empty", "Please fill in empty entries")
            elif pro_name != "" or str(pro_freq) != "" or str(ram) != "" or storage_meth != "":
                messagebox.showwarning("Warning!!!!!", " do you  want to continue without an external gpu?!(Y/N)")
                if opt2 == "Y" or opt2 == "y":
                    root.destroy()
                    import Games_Teir
                elif opt2 == "N" or opt2 == "n":
                    quit()
                else:
                    messagebox.showwarning("Wrong Key", "Enter either Y or N.")


        button = Button(top1, text="Continue", command=new_window)
        button.grid(row=1, column=0, columnspan=2)

        top1.mainloop()

    else:
        messagebox.showerror("Error!!!!!!!", "Andha hai kya bsdk XD")


processor_name_entry.grid(row=0, column=1)
processor_frequency_entry.grid(row=1, column=1)
ram_entry.grid(row=2, column=1)
storage_type.grid(row=3, column=1)
ques.grid(row=4, column=1)

mylabel.grid(row=0, column=0)
mylabel1.grid(row=1, column=0)
mylabel2.grid(row=2, column=0)
mylabel5.grid(row=3, column=0)

queslabel.grid(row=4, column=0)
# print(ram, pro_name, vram, gpu, )


EnterButton = Button(root, text="Enter", padx=80, pady=5, borderwidth=7, command=afterQuestion)

EnterButton.grid(row=7, column=0)
root.mainloop()
