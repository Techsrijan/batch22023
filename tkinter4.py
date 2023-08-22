from tkinter import *
root=Tk()
def test():
    z=arvind.get()
    result.set(z)
    arvind.set('')

lbl=Label(root,text="Enter Your Name",bg="red",fg="white",
          font=("Comic Sans Ms",15,'bold'))
lbl.place(x=100,y=100)
#arvind=StringVar()
arvind=IntVar()
txt=Entry(root,justify='right',font=("Comic Sans Ms",15,'bold'),textvariable=arvind)
txt.place(x=350,y=100)

btn=Button(root,command=test,text="Click Me",bg="red",fg="white",font=("Comic Sans Ms",25,'bold')
           )
btn.place(x=200,y=200)
result=StringVar()
lblres=Label(root,font=("Comic Sans Ms",15,'bold'),textvariable=result)
lblres.place(x=100,y=300)
root.geometry("600x500+420+200")
root.mainloop()