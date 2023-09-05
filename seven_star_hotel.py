from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

taz=Tk()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
#print(h,w)
taz.title("Seven Star Hotel")
user=ImageTk.PhotoImage(Image.open('images/user.png'))
login=ImageTk.PhotoImage(Image.open('images/Login-icon.png'))
############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False



callback = taz.register(only_char_input)  # registers a Tcl to Python callback
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Pyth
# ========mainTreeView======================
tazTV = ttk.Treeview(height=10, columns=('Item Name''Rate','Type'))
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
    lab = Label(taz, text="Seven Star Hotel ", width=30,
                bg="red", fg="black", font=("Comic Sans Ms", "40", "bold"))
    lab.grid(row=0, column=0,columnspan=6)

########## def back ######
def backbutton():
    remove_all_widgets()
    main_heading()
    welcomewindow()



####### OnDoubleClick ######
def OnDoubleClick(event):
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")
    #print(itemNameVar1, item_detail)
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemTypeVar.set(item_detail[1])
#### getIteminTreeView() ####

def getIteminTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="flower")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from item_list"
    mycursor.execute(query)
    data = mycursor.fetchall()
    print(data)
    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"],
                                                               row["item_type"]))
    conn.close()

######## update item ######
def updateItem():
    if itemnameVar.get()=='' or itemrateVar.get()=='' or itemTypeVar.get()=='':
        messagebox.showerror(message="Please Fill all Details")
    else:
        item_name=itemnameVar.get()
        item_rate=itemrateVar.get()
        item_type=itemTypeVar.get()
        dbconnect()
        sqlup="update item_list set item_rate=%s, item_type=%s where item_name=%s"
        val=(item_rate,item_type,item_name)
        mycursor.execute(sqlup, val)
        con.commit()
        con.close()
        messagebox.showinfo(message="Item Updated Successfully")
        itemnameVar.set('')
        itemrateVar.set('')
        itemTypeVar.set('')
        getIteminTreeView()

######### add item #####

def addItem():

    if itemnameVar.get()=='' or itemrateVar.get()=='' or itemTypeVar.get()=='':
        messagebox.showerror(message="Please Fill all Details")
    else:
        item_name=itemnameVar.get().strip().upper()
        item_rate=itemrateVar.get().strip()
        item_type=itemTypeVar.get().strip()
        dbconnect()
        sqlins="insert into item_list(item_name,item_rate,item_type)values(%s,%s,%s)"
        val=(item_name,item_rate,item_type)
        mycursor.execute(sqlins, val)
        con.commit()
        con.close()
        messagebox.showinfo(message="Item Saved Successfully")
        itemnameVar.set('')
        itemrateVar.set('')
        itemTypeVar.set('')
        getIteminTreeView()
###### delete item ######

def deleteItem():
    if itemnameVar.get()=='' or itemrateVar.get()=='' or itemTypeVar.get()=='':
        messagebox.showerror(message="Please Fill all Details")
    else:
        item_name=itemnameVar.get()
        item_rate=itemrateVar.get()
        item_type=itemTypeVar.get()
        dbconnect()
        sqldel="delete from item_list where item_name=%s and item_rate=%s and item_type=%s"
        val = (item_name, item_rate, item_type)
        mycursor.execute(sqldel, val)
        con.commit()
        con.close()
        messagebox.showinfo(message="Item Deleted Successfully")
        itemnameVar.set('')
        itemrateVar.set('')
        itemTypeVar.set('')
        getIteminTreeView()

############add item ############

itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()
def additemwindow():
    remove_all_widgets()
    main_heading()
    welcomeitemLabel = Label(taz, text="Item Details", font="Arial 20")
    welcomeitemLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=1, column=3)

    ###########################
    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)


    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateButton.grid(row=6, column=0)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=addItem)
    additemButton.grid(row=6, column=1, columnspan=2)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10, command=deleteItem)
    deleteButton.grid(row=6, column=3)

    ################# to display treeview ##############################
    tazTV.grid(row=7, column=0, columnspan=3,pady=10)
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=0, columnspan=3,sticky="NSE")
    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getIteminTreeView()
    tazTV.bind("<Double-1>", OnDoubleClick)
######### logout ###############

def adminLogout():
    remove_all_widgets()
    main_heading()
    admin_login()


######### bill generation #########

def billgenerationwindow():
    pass
##### elcome Window ###############
def welcomewindow():
    remove_all_widgets()
    main_heading()
    welcomeLabel = Label(taz, text="Welcome Admin", font="Arial 20")
    welcomeLabel.grid(row=1, column=1, padx=(50, 0), pady=10)

    additemButton = Button(taz, text="Manage Restaurant", width=20, height=2, fg="green", bd=10, command=additemwindow)
    additemButton.grid(row=2, column=0)

    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10,
                        command=billgenerationwindow)
    billButton.grid(row=2, column=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=2, column=2)
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
           #messagebox.showinfo(message='login successful')

        else:
            messagebox.showerror(title="Login Error", message="Either USerName or Password is Incorrect")
            usernameVar.set('')
            passwordVar.set('')



##### admin login window ##### #

usernameVar=StringVar()
passwordVar=StringVar()
def admin_login():
    main_heading()
    loginLabel = Label(taz, text="Admin Login", image=user, compound=BOTTOM,font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username", font="Arial 15")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    userNameEntry = Entry(taz, font="Arial 15", textvariable=usernameVar)
    userNameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password", font="Arial 15")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    passwordEntry = Entry(taz, font="Arial 15", show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    btnLogin = Button(taz, text="Login",image=login, font="Arial 15", fg="white", command=adminLoginProcess)
    btnLogin.grid(row=4, column=1, padx=20, pady=5, columnspan=2)

admin_login()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()