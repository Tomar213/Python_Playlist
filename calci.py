from tkinter import *
import math


def calci():
    def click(event):    
        txt = event.widget.cget("text")
        if txt == "C":
            screen.set("")
        elif txt =="=":
            try:
                result = eval(screen.get())
                screen.set(result)
                entry_screen.update()
            except:            
                screen.set("Error")
        else:
            screen.set(screen.get()+txt)
    

    root= Tk()
    root.title("Scientific calci")
    root.geometry("370x350")
    root.configure(background="cadet blue")
    screen = StringVar()
    screen.set("")
    entry_screen = Entry(root,textvariable=screen ,font="raleway 24 bold",bg="cadet blue")
    entry_screen.pack(padx=10,pady=3)
    can = Canvas(root,width =330,height=290,bg="light gray")
    can.pack()

    b1 = Button(can,text = "1",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b1.bind("<Button-1>",click)
    b1.config()
    can.create_window(25,25,window=b1)

    b2 =Button(can,text = "2",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b2.bind("<Button-1>",click)
    b2.config()
    can.create_window(80,25,window=b2)

    b3 =Button(can,text = "3",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b3.bind("<Button-1>",click)
    b3.config()
    can.create_window(135,25,window=b3)

    b4 =Button(can,text = "4",padx=8,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b4.bind("<Button-1>",click)
    b4.config()
    can.create_window(25,80,window=b4)

    b5 =Button(can,text = "5",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b5.bind("<Button-1>",click)
    b5.config()
    can.create_window(80,80,window=b5)

    b6 =Button(can,text = "6",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b6.bind("<Button-1>",click)
    b6.config()
    can.create_window(135,80,window=b6)

    b7 =Button(can,text = "7",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b7.bind("<Button-1>",click)
    b7.config()
    can.create_window(25,135,window=b7)

    b8 =Button(can,text = "8",padx=10,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b8.bind("<Button-1>",click)
    b8.config()
    can.create_window(80,135,window=b8)

    b9 =Button(can,text = "9",padx=8,pady=8,font="raleway 14 bold",bg="gray",relief=SUNKEN)
    b9.bind("<Button-1>",click)
    b9.config()
    can.create_window(135,135,window=b9)

    b0 =Button(can,text = "0",padx=8,pady=8,font="raleway 13 bold",bg="gray",relief=SUNKEN)
    b0.bind("<Button-1>",click)
    b0.config()
    can.create_window(25,190,window=b0)

    b00 =Button(can,text = "00",padx=8,pady=8,font="raleway 13 bold",bg="gray",relief=SUNKEN)
    b00.bind("<Button-1>",click)
    b00.config()
    can.create_window(80,190,window=b00)

    bC =Button(can,text = "C",padx=8,pady=8,font="raleway 14 bold",bg="sky blue",relief=SUNKEN)
    bC.bind("<Button-1>",click)
    bC.config()
    can.create_window(135,190,window=bC)

    bE =Button(can,text = "=",padx=40,pady=5,font="raleway 20 bold",bg="sky blue",relief=SUNKEN)
    bE.bind("<Button-1>",click)
    bE.config()
    can.create_window(170,255,window=bE)

    bP =Button(can,text = "+",padx=20,pady=5,font="raleway 18 bold",bg="pink",relief=SUNKEN)
    bP.bind("<Button-1>",click)
    bP.config()
    can.create_window(220,25,window=bP)

    bS =Button(can,text = "-",padx=20,pady=5,font="raleway 18 bold",bg="pink",relief=SUNKEN)
    bS.bind("<Button-1>",click)
    bS.config()
    can.create_window(295,25,window=bS)

    bM =Button(can,text = "*",padx=20,pady=5,font="raleway 18 bold",bg="pink",relief=SUNKEN)
    bM.bind("<Button-1>",click)
    bM.config()
    can.create_window(220,90,window=bM)

    bD =Button(can,text = "/",padx=20,pady=5,font="raleway 18 bold",bg="pink",relief=SUNKEN)
    bD.bind("<Button-1>",click)
    bD.config()
    can.create_window(295,90,window=bD)

    bA =Button(can,text = "%",padx=18,pady=5,font="raleway 14 bold",bg="pink",relief=SUNKEN)
    bA.bind("<Button-1>",click)
    bA.config()
    can.create_window(220,145,window=bA)

    def value_sin():
        x = int(screen.get())
        res = math.sin(x)
        screen.set(res)
    def value_cos():
        x = int(screen.get())
        res = math.cos(x)
        screen.set(res)
    def value_tan():
        x = int(screen.get())
        res = math.tan(x)
        screen.set(res)

    bSin =Button(can,text = "Sin(x)",padx=5,pady=10,font="raleway 10 bold",command=value_sin,bg="magenta",relief=SUNKEN)
    bSin.config()
    can.create_window(295,145,window=bSin)
    bCos =Button(can,text = "Cos(x)",padx=10,pady=10,font="raleway 10 bold",command=value_cos,bg="magenta",relief=SUNKEN)
    bCos.config()
    can.create_window(220,193,window=bCos)
    bTan =Button(can,text = "Tan(x)",padx=10,pady=10,font="raleway 10 bold",command=value_cos,bg="magenta",relief=SUNKEN)
    bTan.config()
    can.create_window(295,195,window=bTan)

    root.mainloop()

if  __name__=='__main__':
    calci()

