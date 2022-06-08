from tkinter import *


def data_add():
    file = open("dance_data.txt","a")
    file.write(f"\nName is {name.get()} {lst.get()}\nAge is {age.get()}\nDance plays is {dance.get()}\nAddress is "
               f"{place.get()}\nTiming want {time.get()}\nMentors want {tom.get()}\n\n")
    print("Values added")


root = Tk()
root.geometry("450x450")
f1 = Frame(root,bg="red",borderwidth=3)
f1.grid(row=0,column=0,padx=7)

l1 = Label(f1,text="Dance Academy Registration",relief=SUNKEN,font=("Raleway",22,"bold"),fg="Magenta",bg="black")
l1.grid(row=0,column=3,padx=8)

f2=Frame(root,borderwidth=3)
f2.grid(row=1,column=0)

l2 = Label(f2,text="First Name : ",font=("Normal",12,"bold"),pady=10)
l2.grid(row=0,column=0)
name = StringVar()
nam = Entry(f2,textvariable=name)
nam.grid(row=0,column=1,pady=10)

l3 = Label(f2,text="Last Name : ",font=("Normal",12,"bold"),pady=10)
l3.grid(row=1,column=0)
last = StringVar()
lst = Entry(f2,textvariable=last)
lst.grid(row=1,column=1, pady=10)

l4 = Label(f2,text="Age : ",font=("Normal",12,"bold"),pady=10)
l4.grid(row=2,column=0)
age = StringVar()
ag = Entry(f2,textvariable=age)
ag.grid(row=2,column=1, pady=10)

l5 = Label(f2,text="Dance Type : ",font=("Normal",12,"bold"), pady=10)
l5.grid(row=3,column=0)
dance = StringVar()
dan = Entry(f2,textvariable=dance)
dan.grid(row=3,column=1, pady=10)

l6 = Label(f2,text="Place : ",font=("Normal",12,"bold"), pady=10)
l6.grid(row=4,column=0)
place = StringVar()
pl = Entry(f2,textvariable=place)
pl.grid(row=4,column=1, pady=10)
 #one liners
Label(f2,text="Time suitable : ",font=("Normal",12,"bold"), pady=10).grid(row=5,column=0)
time = StringVar()
Entry(f2,textvariable=time).grid(row=5,column=1, pady=10)
tom = StringVar()
Checkbutton(f2,text="Do you want personal mentoring",variable=tom).grid(row=6,column=1)

Button(f2,text="Submit",command=data_add).grid(row=7,column=0, pady=10)
Button(f2,text="Exit",command=exit).grid(row=7,column=1, pady=10)


root.mainloop()