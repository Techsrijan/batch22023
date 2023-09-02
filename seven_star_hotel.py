from tkinter import *
import pymysql
from tkinter import messagebox

taz=Tk()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
#print(h,w)
taz.title("Seven Star Hotel")

##### remove all widget #########
def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
###### database connectivity##################################
def dbconnect():
    global con,mycursor
    con = pymysql.connect(host='localhost', user='root', db='flower')
    #print("Connection mil gaya")
    mycursor = con.cursor()
######### main heading #######################
def main_heading():
    lab = Label(taz, text="             Seven Star Hotel                             ",
                bg="red", fg="black", font=("Comic Sans Ms", "40", "bold"))
    lab.grid(row=0, column=0,columnspan=6)

##### elcome Window ###############
def welcomewindow():
    remove_all_widgets()
    main_heading()
    welcomeLabel = Label(taz, text="Welcome Admin", font="Arial 20")
    welcomeLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)
########### admin login Process #####
def adminLoginProcess():
    if usernameVar.get()=='' or passwordVar.get()=='':
        messagebox.showerror(title="Login Error",message="Please enter User Name and Password Both")
    else:
        user=usernameVar.get()
        pwd=passwordVar.get()
        dbconnect()
        que = "select * from login where binary username=%s and binary password=%s"
        val = (user, pwd)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        #print(data)
        flag = False
        for row in data:
            flag = True

        con.close()
        if flag == True:
           welcomewindow()
           messagebox.showinfo(message='login successful')

        else:
            messagebox.showerror(title="Login Error", message="Either USerName or Password is Incorrect")
            usernameVar.set('')
            passwordVar.set('')



##### admin login window ##### #

usernameVar=StringVar()
passwordVar=StringVar()
def admin_login():
    main_heading()
    loginLabel = Label(taz, text="Admin Login", font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username", font="Arial 15")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    userNameEntry = Entry(taz, font="Arial 15", textvariable=usernameVar)
    userNameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password", font="Arial 15")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    passwordEntry = Entry(taz, font="Arial 15", show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    btnLogin = Button(taz, text="Login", font="Arial 15", bg="green", fg="white", command=adminLoginProcess)
    btnLogin.grid(row=4, column=1, padx=20, pady=5, columnspan=2)

admin_login()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()