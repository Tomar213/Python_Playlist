from tkinter import *
import mysql.connector
dba = mysql.connector.connect(host="localhost",user = "root", passwd = "0000", db = "python_db")


def hello():
    print(f"Hi there its tkinter")


def gett():
    mycusr = dba.cursor()
    q = "insert into rampur (name,numb) values(%s,%s)"
    val = (f"{user.get()}",f"{password.get()}")
    mycusr.execute(q,val)
    dba.commit()
    print(f"username is: {user.get()}")
    print(f"password is: {password.get()}")


root = Tk()
root.geometry("650x500")
root.title("My GUI with Harry bhai")
# set image
# pics = PhotoImage(file="Screenshot (11).png")
# label = Label(image=pics)
# label.pack(side="left")

title_label = Label(text="MY FIRST EVER GUI ", bg="Light Gray", fg="Black", padx=10, pady=250, font=("raleway", 10, "bold"),
                    borderwidth =5, relief=SUNKEN)
title_label.pack(side="left",fill=Y)
label2 = Label(text="Here we are learning python and currently we are on the GUI chapter of the Whole series ",borderwidth=3, bg="gray",)
label2.pack(anchor="se",side="bottom",fill=X,padx=10)
f2= Frame(root,bg="black",borderwidth=3)
f2.pack(side="top")
label4 = Label(f2,text="this is the heading",relief=SUNKEN,fg="Magenta",padx=100,font="Bold")
label4.pack(side="top")

f3=Frame(root,borderwidth=5,bg="blue")
f3.pack()

f1= Frame(root,bg="gray",borderwidth=3)
f1.pack(anchor="se")
label3 = Label(f1,text="this is a text editor ",relief=SUNKEN)
label3.pack(padx=20)

f_grid = Frame(root)
f_grid.pack(anchor="nw")


label6 = Label(f_grid,text="user")
label6.grid()
label5 = Label(f_grid,text="password")
label5.grid()
#
user = StringVar()
password = StringVar()
#
ent1 = Entry(f_grid,textvariable=user)
ent2=Entry(f_grid,textvariable=password)
ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)

b4= Button(f_grid,text="print",command=gett)
b4.grid(row=4,column=0)


b1 = Button(f3,text="Button", command=hello)
b1.pack(side=LEFT)
b2 = Button(f3,text="Button2", command=hello)
b2.pack(side=LEFT)
b3= Button(f3,text="Button3", command=hello)
b3.pack(side="bottom")
root.mainloop()
