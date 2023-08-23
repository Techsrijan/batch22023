from tkinter import *

def add(event=''):
    a=first.get()
    b=second.get()
    c=int(a)+int(b)
    result.set(c)
    data.set(c)
    # first.set('')
    # second.set('')
    # print(c)
    # print(a,b)

def sub():
    a = first.get()
    b = second.get()
    c = int(a) - int(b)
    result.set(c)
    data.set(c)
    # first.set('')
    # second.set('')
root=Tk()

root.bind("<Control-a>",add)
root.bind("<Control-A>",add)

root.title("My Calci")
root.iconbitmap('cal.ico')
lbl=Label(root,text="Enter first Number",
          font=("Comic Sans Ms",12,'bold'))
lbl.grid(row=0,column=0)
first=StringVar()
ent=Entry(root,font=("Comic Sans Ms",12,'bold'),textvariable=first)
ent.grid(row=0,column=1)


lbl2=Label(root,text="Enter Second Number",
          font=("Comic Sans Ms",12,'bold'))
lbl2.grid(row=1,column=0)

second=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",12,'bold'),textvariable=second)
ent2.grid(row=1,column=1)

btn=Button(root,text="+",font=("Comic Sans Ms",12,'bold'),
           bg='red',fg='yellow',width=20,bd=5,command=add)
btn.grid(row=2,column=0)


btn2=Button(root,text="Subtract",font=("Comic Sans Ms",12,'bold'),
           bg='red',fg='yellow',width=20,bd=5,command=sub)
btn2.grid(row=2,column=1)


result=StringVar()
res=Label(root,font=("Comic Sans Ms",12,'bold'),fg='blue',textvariable=result)
res.grid(row=3,column=0)

data=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",12,'bold'),textvariable=data)
ent2.grid(row=3,column=1)

btn33=Button(root,text="Subtract",font=("Comic Sans Ms",12,'bold'),
           bg='red',fg='yellow',width=20,bd=5)
btn33.grid(row=4,column=0,columnspan=2)
root.resizable(0,0)

root.mainloop()