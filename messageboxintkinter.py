from tkinter import *
from tkinter import messagebox
root=Tk()
def open_message():
    res=messagebox.showwarning(title="Notepad",message="Do u want to save this file?")
    print(res)
    if res==True:
        print("file saved")
    elif res==False:
        print("File not saved")

btn=Button(root,text="Close",command=open_message)
btn.pack()
root.geometry("400x400+150+150")
root.mainloop()