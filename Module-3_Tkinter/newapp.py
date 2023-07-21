from tkinter import *
from tkinter import ttk,Tk,messagebox


screen=Tk()
screen.geometry('500x500')
screen.config(bg='gold')
screen.title("NewApp")

def btnClick():
    print("This is Button")
    print(f"FirstName:{fnm.get()}")
    print(f"Lastname:{lnm.get()}")
    #messagebox.showerror(title="Error",message="Something went wrong...Try again!")
    #messagebox.showwarning(title="Warning",message="Your disk is full!")
    #messagebox.showinfo(title="Success",message="Signup Successfully!")

    #messagebox.askokcancel(title="Download",message="Do you want to continue?")
    #messagebox.askquestion(title="Download",message="Do you want to continue?")
    #messagebox.askretrycancel(title="Download",message="Do you want to continue?")
    #messagebox.askyesno(title="Download",message="Do you want to continue?")
    #messagebox.askyesnocancel(title="Download",message="Do you want to continue?")



Label(text="Firstname:",bg='gold',font='Cooper 15 bold').grid(row=0,column=0,sticky='W')
Label(text="Lastname:",bg='gold',font='Cooper 15 bold').grid(row=1,column=0,sticky='W')

fnm=Entry(screen,font='Cooper 15 bold')
fnm.grid(row=0,column=1,sticky='W')
lnm=Entry(screen,font='Cooper 15 bold')
lnm.grid(row=1,column=1,sticky='W')

Radiobutton(text="Male",value=0,bg='gold',font='Cooper 15 bold').grid(row=2,column=0,sticky='W')
Radiobutton(text="Female",value=1,bg='gold',font='Cooper 15 bold').grid(row=2,column=1,sticky='W')

Checkbutton(text="Reading",bg='gold',font='Cooper 15 bold').grid(row=3,column=0,sticky='W')
Checkbutton(text="Movie",bg='gold',font='Cooper 15 bold').grid(row=4,column=0,sticky='W')
Checkbutton(text="Travelling",bg='gold',font='Cooper 15 bold').grid(row=5,column=0,sticky='W')
Checkbutton(text="Video Games",bg='gold',font='Cooper 15 bold').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Baroda','Rajkot','Surat','Jamnagar','Junagadh']
ttk.Combobox(values=city).grid(row=7,column=0,sticky='W')

Button(text='Submit',font='Cooper 15 bold',command=btnClick).place(x=180,y=300)
screen.mainloop()