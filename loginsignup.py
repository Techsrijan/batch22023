from tkinter import *
import pymysql
from tkinter import messagebox

def dbconnect():
    global con,mycursor
    con = pymysql.connect(host='localhost', user='root', db='flower')
    #print("Connection mil gaya")
    mycursor = con.cursor()
def gettext():
    dbconnect()
    c=a.get()
    d =b.get()
    sqlins="insert into login(username,password) values(%s,%s)"
    val=(c,d)
    mycursor.execute(sqlins,val)
    con.commit()
    messagebox.showinfo(title="Data Insertion",message="Data Inserted")
    a.set('')
    b.set('')
    #print(c,d)
root=Tk()
l=Label(root,text="Enter User Name",
        font=("Comic Sans Ms",15,"bold"))
l.grid(row=0,column=0)

a=StringVar()
txt=Entry(root,bd="10",font=("Comic Sans Ms",15,"bold"),textvariable=a)
txt.grid(row=0,column=1,pady=10)


l2=Label(root,text="Enter Password",
        font=("Comic Sans Ms",15,"bold"))
l2.grid(row=1,column=0)
b=StringVar()
txt2=Entry(root,bd="10",font=("Comic Sans Ms",15,"bold"),textvariable=b)
txt2.grid(row=1,column=1,pady=10)

btn4=Button(root,text="Create Account",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"),command=gettext)
btn4.grid(row=2,column=0,columnspan=2)

result=StringVar()
l3=Label(root,
        font=("Comic Sans Ms",15,"bold"),textvariable=result)
l3.grid(row=3,column=0,columnspan=2)
root.geometry("+300+200")
root.mainloop()