from cProfile import label
from tkinter import *
import tkinter.messagebox as tkmsg

def sett():
    rot.geometry(f"{wid.get()}x{hei.get()}")

rot = Tk()
width_ = 400
height_ = 400
rot.geometry(f"{width_}x{height_}")
rot.title("clip board")

def hel():
    print("this is from menu")
def heelp():
    print("karan will assist you here")
    tkmsg.showinfo("Help","you are being assisted by karan thakur ")     # this will just show the message and return ok
def qsn():
   val= tkmsg.askquestion("How was your experience","would you continue next time ")   #this return yes or no
   if val=="yes":
       tkmsg.showinfo("Rating","Rate us on App store ")
   else:
       tkmsg.showwarning("opolise","we will definately improve our GUI")

# creating menu 
mymenu = Menu(rot)

m1 = Menu(mymenu,tearoff=0)
m1.add_command(label = "save",command=hel)
m1.add_command(label = "save as",command=hel)
m1.add_command(label = "print",command=hel)
m1.add_command(label = "open",command=hel)
m1.add_command(label = "recent",command=hel)
m1.add_command(label = "new",command=hel)

m2 = Menu(mymenu,tearoff=0)
m2.add_command(label = "save",command=hel)
m2.add_command(label = "save as",command=hel)
m2.add_command(label = "print",command=hel) 
m2.add_command(label = "open",command=hel)

m3 = Menu(mymenu,tearoff=0)
m3.add_command(label = "assistnant",command = heelp)
m3.add_command(label = "Feedback",command =qsn)
m3.add_command(label = "EXIT",command =quit)

rot.config(menu=mymenu)
mymenu.add_cascade(label = "File",menu=m1)
mymenu.add_cascade(label = "Edit",menu=m2)
mymenu.add_cascade(label = "Help",menu = m3)


can = Canvas(rot,width=f"{width_}",height=f"{height_}")
can.pack()
wid = StringVar()
hei = StringVar()
l1=Label(can,text="WIDTH :")
l1.config(font=("helvetica",10))
can.create_window(50,20,window=l1)
l2=Label(can,text="HEIGHT :")
l2.config(font=("helvetica",10))
can.create_window(50,45,window=l2)
e1 = Entry(can,textvariable=wid)
e1.config()
can.create_window(160,20,window=e1)
e2 = Entry(can,textvariable=hei)
e2.config()
can.create_window(160,45,window=e2)
b1 = Button(can,text="set size",command=sett)
b1.config()
can.create_window(100,80,window=b1)
rot.mainloop()  