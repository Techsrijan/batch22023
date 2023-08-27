# Import Required Library
from tkinter import *
import win32api
from tkinter import filedialog

# Create Tkinter Object
root = Tk()

# Set Title and geometry
root.title('Print Hard Copies')
root.geometry("200x200")


# Print File Function
def print_file():
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
        initialdir="/", title="Select file",
        filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

    if file_to_print:
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


# Make Button
Button(root, text="Print FIle", command=print_file).pack()

# Execute Tkinter
root.mainloop()
