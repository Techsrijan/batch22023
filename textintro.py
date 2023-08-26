from tkinter import *
from tkinter import filedialog,colorchooser

def getData():
    c=txt.get(1.0,END)
    print(c)

def opencolor():
    a=colorchooser.askcolor()
    #txt.configure(background=(a[1]))
    txt.configure(foreground=(a[1]))
    # txt.foreground()
    print(a)
def delData():
    txt.delete(1.0,END)

def openFile():
    x=filedialog.askopenfile(title="open txt file",initialdir="/",mode="r",
                             filetypes=(("AllFiles","*.*"),("TextFile","*.txt")))
    for data in x:
        #print(data)
        txt.insert(INSERT,data)
root=Tk()

txt=Text(root,wrap=WORD,selectbackground='red')
#txt.pack(fill=BOTH,expand=1)
txt.pack()


btn4=Button(root, text="color",command=opencolor)
btn4.pack()
btn3=Button(root, text="open file",command=openFile)
btn3.pack()

btn=Button(root, text="get text data",command=getData)
btn.pack()
btn2=Button(root, text="delete data",command=delData)
btn2.pack()


#txt.insert(INSERT,"hello")
root.geometry("500x800+120+120")



root.mainloop()