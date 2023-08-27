from tkinter import *
root=Tk()
can=Canvas(root,bg='white',height=800, width=800)
# l=can.create_line(10,10,200,300,width=12,fill='red')
# r=can.create_rectangle(10,10,200,300)
# c=can.create_oval(10,10,200,200,fill='blue')


photo=PhotoImage(file="best.gif")
can.create_image(10,100,image=photo,anchor=NW)



can.pack()
root.geometry("800x800+120+120")
root.mainloop()