import tkinter
from tkinter import ttk

scr=tkinter.Tk()
scr.title("FirstApp")
scr.geometry("500x500")
scr.config(background="lightblue")

"""tkinter.Label(text="Firstname").pack()
tkinter.Label(text="Lastname").pack()"""

"""tkinter.Label(text="Firstname:",bg='lightblue',font='Fixedsys 15 bold',fg='purple').place(x=0,y=0)
tkinter.Label(text="Lastname:",bg='lightblue',font='Fixedsys 15 bold',fg='purple').place(x=0,y=30)"""

tkinter.Label(text="Firstname:",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=1,column=0,sticky='w')

tkinter.Entry().grid(row=0,column=1,sticky='w')
tkinter.Entry().grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text="Male",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Python",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="PHP",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="Android",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=5,column=0,sticky='w')
tkinter.Checkbutton(text="iOS",bg='lightblue',font='Fixedsys 15 bold',fg='purple').grid(row=6,column=0,sticky='w')

city=['Rajkot','Baroda','Ahmedabad','Surat','Junagadh']
ttk.Combobox(values=city).grid(row=7,column=0)

def btnclick():
    print("This is button!")

tkinter.Button(text="Submit",font='Fixedsys 15 bold',command=btnclick).place(x=200,y=250)
tkinter.mainloop()