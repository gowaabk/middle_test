from tkinter import *

import lib

window = Tk()
window.title("NoteApp")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

table_frame = Frame(window)
table_frame.pack(anchor=N)

buttons_frame = Frame(window)
buttons_frame.pack(anchor=S)
#buttons_frame.place(height=100, width=100)

table = lib.Table(table_frame)
buttons = lib.Buttons(buttons_frame, table)

window.mainloop()
