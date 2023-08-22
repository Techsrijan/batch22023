from tkinter import *
root=Tk()
def test():
    print("hi")
    print(arvind.get())

lbl=Label(root,text="Enter Your Name",bg="red",fg="white",
          font=("Comic Sans Ms",25,'bold'))
lbl.pack()
#arvind=StringVar()
arvind=IntVar()
txt=Entry(root,justify='right',show="?",font=("Comic Sans Ms",25,'bold'),textvariable=arvind)
txt.pack()

btn=Button(root,command=test,text="Click Me",bg="red",fg="white",font=("Comic Sans Ms",25,'bold')
           )
btn.pack()
root.geometry("400x500+420+200")
root.mainloop()