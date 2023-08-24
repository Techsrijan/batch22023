from tkinter import *
root=Tk()
def test():
    print("Menu bar is working")
main_menu=Menu(root)
root.config(menu=main_menu)
# file menu
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+N",command=test)
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit",accelerator="Ctrl+X",command=quit)
#edit menu
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="EDIT",menu=edit_menu)
edit_menu.add_command(label="Cut",accelerator="Ctrl+X")
edit_menu.add_command(label="Copy")

root.geometry("400x500+320+120")
root.mainloop()