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
          font=("Comic Sans Ms",12,'bold'),bg='blue',fg='white')
lbl.place(x=80,y=100)
first=StringVar()
ent=Entry(root,font=("Comic Sans Ms",12,'bold'),textvariable=first)
ent.place(x=325,y=100)


lbl2=Label(root,text="Enter Second Number",
          font=("Comic Sans Ms",12,'bold'),bg='blue',fg='white')
lbl2.place(x=80,y=200)

second=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",12,'bold'),textvariable=second)
ent2.place(x=325,y=200)

btn=Button(root,text="+",font=("Comic Sans Ms",12,'bold'),
           bg='red',fg='yellow',width=20,bd=25,command=add)
btn.place(x=200,y=250)


btn2=Button(root,text="Subtract",font=("Comic Sans Ms",12,'bold'),
           bg='red',fg='yellow',width=20,bd=25,command=sub)
btn2.place(x=400,y=250)


result=StringVar()
res=Label(root,font=("Comic Sans Ms",12,'bold'),fg='blue',textvariable=result)
res.place(x=200,y=400)

data=StringVar()
ent2=Entry(root,font=("Comic Sans Ms",12,'bold'),textvariable=data)
ent2.place(x=325,y=400)
root.resizable(0,0)
root.geometry("800x500+120+120")
root.mainloop()