from tkinter import *

class Mywindow:
    def __init__(self,window):
        self.window=window
        self.btn=Button(self.window,text="click me")
        self.btn.pack()




root=Tk()
t=Mywindow(root)
root.mainloop()