from tkinter import *

def openwindow():
    t=Toplevel(root)
    btn3 = Button(t, text="close App", command=t.destroy).pack()
    t.geometry("400x500+120+120")
root=Tk()


root.geometry("400x500+120+120")


btn2=Button(root,text="open window",command=openwindow).pack()
btn3=Button(root,text="close App",command=quit).pack()
root.geometry("400x500+120+120")
root.mainloop()