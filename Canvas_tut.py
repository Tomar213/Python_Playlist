from tkinter import *
root = Tk()


def regis(self):
    import danceAcadmy


height_canvas = 400
width_canvas = 500
root.geometry("500x550")        # width x height
root.title("Gui using Canvas")
can = Canvas(root, width=width_canvas,height=height_canvas)
can.pack()
can.create_line(00,20,500,20,fill="black")   # coordinates are from starting(x1,y1) to  end(x2,y2)
can.create_text(70,10,text="Here We Go",fill="red",font=("raleway",15,"bold"))  # cordinates are of center of the text
can.create_text(30,90,text="Rectange",fill="black",font=("raleway",10))
can.create_rectangle(0,100,400,200,fill= "yellow")   # cordinates are of left top  and right bottom
b = Button(root,text ="double click to exit")
b.pack(anchor="nw")
b.bind('<Double-1>',quit)
b2 = Button(root,text ="CLICK TO REGISTER")
b2.pack(anchor="nw")
b2.bind('<Button-1>',regis)
root.mainloop()


