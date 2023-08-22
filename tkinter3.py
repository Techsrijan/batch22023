from tkinter import *
root=Tk()


btn=Button(root,text="Click Me1",bg="red",fg="white",
           font=("Comic Sans Ms",10,'bold'),bd=50)
btn.pack(side='top', fill='x')
btn1=Button(root,text="Click Me2",bg="green",fg="white",
           font=("Comic Sans Ms",25,'bold'))
btn1.pack(side='left',fill='y')

btn2=Button(root,text="Click Me3",bg="red",fg="white",
           font=("Comic Sans Ms",25,'bold'))
btn2.pack(side='right',fill='y')

btn3=Button(root,text="Click Me4",bg="red",fg="white",
           font=("Comic Sans Ms",25,'bold'))
btn3.pack(side='bottom',fill='x')
root.geometry("400x500+420+200")
root.mainloop()