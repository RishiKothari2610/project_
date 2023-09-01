# from tkinter import *
# root = Tk()
# root.geometry("1000x700")
# root.title("Registration Form")

# Frame(root, width=1300, height=1200, bg='white').place(x=0, y=0)


# Label(root, text="Name:" ,bg="white").place(x=200,y=200)
# Label(root, text="Email:", bg="white").place(x=200, y=300)
# Label(root, text="Password:", bg="white").place(x=200, y=400)
# name_entry = Entry(root,border=0,bg='white')
# Frame(root, width=290, height=2, bg='black').place(x=250, y=225)
# name_entry.place(x=250, y=200)
# name_entry.insert(0,'name')
# root.mainloop()

import tkinter as tk

root = tk.Tk()

# Create a Label widget with right-aligned text
label = tk.Label(root, text="Right-aligned text", justify='right')
label.pack()

root.mainloop()
