from tkinter import *
from tkinter import simpledialog

root=Tk()
def getData():
    print(sc.get())
    print(sp.get())

def getmarks():
    sum=0
    n=int(input("How many students u have"))
    for i in range(n):
        x=simpledialog.askinteger(title="input Marks",prompt="enter marks")
        sum=sum+x
    print(sum)
sc=Scale(root,from_=1000, to=5000,orient=HORIZONTAL,length=200,sliderlength=50,width=25)
sc.set(25)
sc.pack()

sp=Spinbox(root,from_=1,to=5)
sp.pack()

btn=Button(root,text="get Data",command=getData).pack()
root.geometry("400x500+120+120")


btn2=Button(root,text="get Marks",command=getmarks).pack()
root.geometry("400x500+120+120")
root.mainloop()