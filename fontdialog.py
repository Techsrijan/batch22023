import tkinter as tk
from tkinter import font


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # persistent font reference
        textfont = font.Font(family='arial', size='14')

        # something to type in ~ uses the persistent font reference
        tk.Text(self, font=textfont).grid(row=0, column=0, sticky='nswe')

        # make the textfield fill all available space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # font chooser
        fc = tk.Listbox(self)
        fc.grid(row=0, column=1, sticky='nse')

        # insert all the fonts
        for f in font.families():
            fc.insert('end', f)

        # switch textfont family on release
        fc.bind('<ButtonRelease-1>', lambda e: textfont.config(family=fc.get(fc.curselection())))

        # scrollbar ~ you can actually just use the mousewheel to scroll
        vsb = tk.Scrollbar(self)
        vsb.grid(row=0, column=2, sticky='ns')

        # connect the scrollbar and font chooser
        fc.configure(yscrollcommand=vsb.set)
        vsb.configure(command=fc.yview)


if __name__ == "__main__":
    app = App()
    app.title('Font Chooser Example')
    app.geometry(f'800x600+200+200')
    app.mainloop()
