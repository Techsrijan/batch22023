from tkinter import *
from tkinter import ttk
root=Tk()
def getData():
    print(c.get())
l=[]
for i in range(1,32):
    l.append(i)
c=ttk.Combobox(root,values=l,state='readonly',height=5,width=5)
c.set('Select Course')
c.pack()

btn=Button(root,text="Get Data",command=getData)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()
