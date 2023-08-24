from tkinter import *
from tkinter import ttk
root=Tk()
def getData():
    if i.get()=='male':
        print("Male")
    else:
        print("female")

i=StringVar()
lf=LabelFrame(root,text="Select gender")
r1=Radiobutton(lf,text="Male",value='male',variable=i)
r1.pack()
r2=Radiobutton(lf,text="Female",value='female',variable=i)
r2.pack()
lf.pack()
j=IntVar()
r3=Radiobutton(root,text="Govt",value=1,variable=j)
r3.pack()
r4=Radiobutton(root,text="Private",value=2,variable=j)
r4.pack()

btn=Button(root,text="Get Data",command=getData)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()
