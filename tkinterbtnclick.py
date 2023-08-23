from tkinter import *

def rightclick(event):
    print("right click is pressed")


def middleclick(event):
    print("middle click is pressed")


def leftclick(event):
    print("left click is pressed")
root=Tk()



btn=Button(root,text="right click", bg='red',fg='white',width=20,bd=25,font=("Comic Sans Ms",12,'bold'))
btn.pack()

btn1=Button(root,text="middle click", bg='red',fg='white',width=20,bd=25,font=("Comic Sans Ms",12,'bold'))
btn1.pack()

btn2=Button(root,text="left click", bg='red',fg='white',width=20,bd=25,font=("Comic Sans Ms",12,'bold'))
btn2.pack()

btn.bind("<Button-3>",rightclick)

btn1.bind("<Button-2>",middleclick)

btn2.bind("<Button-1>",leftclick)
root.mainloop()