import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


# function_Area
def newFile():
    global file
    window.title("Untitled - Notepad")
    file = None
    txt_area.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + "- Notepad")
        txt_area.delete(1.0, END)
        f = open(file, "r")
        txt_area.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(txt_area.get(1.0, END))
            f.close()

            window.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(txt_area.get(1.0, END))
        f.close()


def cutText():
    txt_area.event_generate("<<Cut>>")


def copyText():
    txt_area.event_generate("<<Copy>>")


def pasteText():
    txt_area.event_generate("<<Paste>>")


def searchText():
    pass


def about():
    showinfo("About Us", "Software is Developed By Bageesh Sharma & Team")


if __name__ == '__main__':
    window = Tk()
    # Set Title
    window.title("Untitled - Notepad")

# Window Size
window.geometry("644x788")
window.minsize(300, 300)
window.maxsize(850, 600)
# Window Size End

# Area_Menu Starts
menu_bar = Menu(window)
window.config(menu=menu_bar)

# File Menu Starts
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_separator()
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_separator()
menu_bar.add_cascade(label="File", menu=file_menu)
# File Menu End

# Edit Menu Start
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cutText)
edit_menu.add_command(label="Copy", command=copyText)
edit_menu.add_command(label="Paste", command=pasteText)
edit_menu.add_separator()
edit_menu.add_command(label="Find..", command=searchText)
edit_menu.add_separator()
menu_bar.add_cascade(label="Edit", menu=edit_menu)
# Edit Menu End

# About Menu Start
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About Notepad", command=about)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_separator()
# About Menu End

# Exit Button End
menu_bar.add_command(label="Exit", command=quit)
# Exit Button End

# Area_Menu Ends

# Text Area Start
txt_area = Text(window, font="Arial 13")
file = None
txt_area.pack(expand=True, fill=BOTH)
# Text Area End

# Scroll Bar Starts
Scroll_bar = Scrollbar(txt_area)
Scroll_bar.pack(side=RIGHT, fill=Y)
Scroll_bar.config(command=txt_area.yview)
txt_area.config(yscrollcommand=Scroll_bar.set)
# Scroll Bar Ends

window.mainloop()