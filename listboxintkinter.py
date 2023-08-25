from tkinter import *
root=Tk()
# def addData():
#     c=a.get()
#     l.insert(END,c)

def getData():
    a=l.curselection()
    print(a)
    for data in a:
        print(l.get(data))




def deleteData():
    a = l.curselection()
    for data in a:
        print(l.delete(data))


def clearData():
    #l.delete('first','last')
    pass

f=Frame(root)
scroll=Scrollbar(f)

l=Listbox(f,height=10,yscrollcommand=scroll.set,
          selectmode=EXTENDED) # SINGLE BROWSE, MULTIPLE, EXTENDED


scroll.config(command=l.yview)
scroll.pack(side=RIGHT,fill=Y)


for i in range(23):
    l.insert(END,"Happy b-day="+str(i))
l.pack()
f.pack()
'''
a=StringVar()
txt=Entry(root,font=("Comic Sans Ms",25,'bold'),
          textvariable=a)
txt.pack()
btn=Button(root,text="Click Me1",bg="red",fg="white",
           font=("Comic Sans Ms",10,'bold'),bd=50,command=addData)
btn.pack(side='top', fill='x')
'''

btn=Button(root,text="Get Data",bg="red",fg="white",
           font=("Comic Sans Ms",10,'bold'),bd=50,command=getData)
btn.pack(side='top')

btn1=Button(root,text="Delete Data",bg="red",fg="white",
           font=("Comic Sans Ms",10,'bold'),bd=50,command=deleteData)
btn1.pack(side='top')

btn3=Button(root,text="Clear Data",bg="red",fg="white",
           font=("Comic Sans Ms",10,'bold'),bd=50,command=clearData)
btn3.pack(side='top')
root.geometry("400x800+150+150")
root.mainloop()