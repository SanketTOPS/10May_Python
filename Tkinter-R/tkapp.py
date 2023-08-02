import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()
screen.title("FirstApp")
screen.geometry('400x500')
screen.config(bg='gold')

"""tkinter.Label(text='Firstname').pack()
tkinter.Label(text='Lastname').pack()"""


"""tkinter.Label(text='Firstname:',font='Bahnschrift 15 bold',bg='gold').place(x=0,y=0)
tkinter.Label(text='Lastname:',font='Bahnschrift 15 bold',bg='gold').place(x=0,y=30)"""

tkinter.Label(text='Firstname:',font='Bahnschrift 15 bold',bg='gold').grid(row=0,column=0,sticky='W')
tkinter.Label(text='Lastname:',font='Bahnschrift 15 bold',bg='gold').grid(row=1,column=0,sticky='W')

fnm=tkinter.Entry()
fnm.grid(row=0,column=1,sticky='W')
lnm=tkinter.Entry()
lnm.grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text='Male',font='Bahnschrift 15 bold',bg='gold').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text='Female',font='Bahnschrift 15 bold',bg='gold').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Gujarati',font='Bahnschrift 15 bold',bg='gold').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='Hindi',font='Bahnschrift 15 bold',bg='gold').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='English',font='Bahnschrift 15 bold',bg='gold').grid(row=5,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Junagadh','Jamnagar']
ttk.Combobox(values=city).grid(row=6,column=0,sticky='W')

def btnclick():
    #print("Button click!")
    #messagebox.showerror("Error","Something went wrong...Try again!")
    #messagebox.showinfo("Success","Signup Successfully!")
    #messagebox.showwarning("Warning","Disk is full!")

    #messagebox.askokcancel("Download","Do you want to continue?")
    #messagebox.askquestion("Download","Do you want to continue?")
    #messagebox.askretrycancel("Download","Do you want to continue?")
    #messagebox.askyesno("Download","Do you want to continue?")
    #messagebox.askyesnocancel("Download","Do you want to continue?")

    #get value of textfields
    print(f"Firstname:{fnm.get()}")
    print(f"Lastname:{lnm.get()}")
    messagebox.askyesnocancel("Fullname",f"{fnm.get()}+' '+{lnm.get()}")



tkinter.Button(command=btnclick,text='Submit',font='Bahnschrift 15 bold').place(x=170,y=280)
tkinter.mainloop()