from tkinter import *
from mysql import *
import mysql.connector as m
import tkinter.messagebox as tkmsg


conn = m.connect(host="localhost",user= "root",passwd="0000",db="python_db")

def upload():
    curs = conn.cursor()
    q= f"insert into rampur (name,numb) values(%s,%s)"
    val = (f"{nam.get()}",f"{slid.get()}")
    curs.execute(q,val)
    conn.commit()
    tkmsg.showinfo("chinese Restro","Your feedback is so worthful \n THANK YOU ! \n VISIT AGAIN")


rot = Tk()
rot.geometry("350x300")
rot.title("Chinese Restro")

can = Canvas(rot,width=400,height=300)
can.configure(background="yellow")
can.pack()
l1 = Label(can,text="THANK YOU FOR VISITING US",font=("helvetica",15,"bold"),fg="GREEN")
l1.config(pady=5)
can.create_window(170,20,window=l1)
l2 = Label(can,text= "kindly Give your Feedback ")
l2.config()
can.create_window(150,50,window=l2)
slid = Scale(can,from_=0,to="10",orient=HORIZONTAL,tickinterval=2)
slid.set(5)
slid.config()
can.create_window(150,90,window=slid)

l2 = Label(can,text= "Your name : ")
l2.config()
can.create_window(70,140,window=l2)

nam = StringVar()
e1 = Entry(can,textvariable=nam)
e1.config()
can.create_window(170,140,window=e1)

b= Button(can,text="Submit",command=upload)
b.config()
can.create_window(110,180,window=b)
can.create_rectangle(8,8,330,220)

b1= Button(can,text="Exit",command=quit)
b1.config()
can.create_window(160,180,window=b1)
can.create_rectangle(8,8,330,220)

rot.mainloop()