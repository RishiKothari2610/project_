import tkinter as tk


def focus_in(event):
    event.widget.configure(background="light blue")


def focus_out(event):
    event.widget.configure(background="white")


def submit():
    # code to submit the form
    print("Form submitted!")


root = tk.Tk()
root.geometry("300x200")
root.title("Registration Form")

# labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Password:").grid(row=2, column=0, padx=5, pady=5)

# entries
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.bind("<FocusIn>", focus_in)
name_entry.bind("<FocusOut>", focus_out)

email_entry = tk.Entry(root,border=0)
temp = tk.LabelFrame(root,width=295,height=2,bg='black')
temp.place(z=25,y=107,relx=0.5,rely=0.5)
email_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry.bind("<FocusIn>", focus_in)
email_entry.bind("<FocusOut>", focus_out)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)
password_entry.bind("<FocusIn>", focus_in)
password_entry.bind("<FocusOut>", focus_out)

# button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
