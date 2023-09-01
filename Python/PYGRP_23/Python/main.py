from tkinter import *
from tkinter import simpledialog
import tkinter as tk
from tkinter import messagebox
# Pandas library to work with Excel as a database
import pandas as pd
# python imaging library(PIL) to process images for buttons and backgrounds of windows
from PIL import ImageTk, Image
# Random import to generate random OTPs and Account Numbers
import random
# SMTP server library to send emails
import smtplib
from email.mime.text import MIMEText
# date and time imports for transaction history
from pytz import timezone
from datetime import datetime
# to speak about transactions
from gtts import gTTS
import pyttsx3
import os

EXCEL_FILE = 'BankDB.xlsx'
CENTER = 'center'

class User:

    def __init__(self, first, middle, last, DOB, email, mob, gender, aadharNo, accNo, password, balance):
        self.first = first
        self.middle = middle
        self.last = last
        self.DOB = DOB
        self.email = email
        self.mob = mob
        self.gender = gender
        self.aadharNo = aadharNo
        self.accNo = accNo
        self.password = password
        self.balance = balance
        User.add(self)

    def add(self):
        ask = messagebox.askokcancel("Recheck Please!", "Are you sure?")
        if (not ask):
            return

        df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
        randOTP = random.randint(1000, 9999)
        print(randOTP)
        msgstr = "Your OTP is : " + str(randOTP)
        SendEmail(self.email, 'Verification OTP', msgstr)
        otp = simpledialog.askstring(
            title="OTP", prompt="Check your Email for OTP")
        print(otp, self.gender, self.accNo)
        if (int(otp) == randOTP):
            print("Continue user is safe")
            name = self.first + ' ' + self.middle + ' ' + self.last
            data = {
                'Account Number': str(self.accNo),
                'Password': self.password,
                'Name': self.first+' '+self.middle+' '+self.last,
                'DOB': self.DOB,
                'Email': self.email,
                'Mobile Number': self.mob,
                'Gender': self.gender,
                'Aadhar Number': self.aadharNo,
                'Balance': self.balance
            }
            print('data created\n', data)
            df = df.append(data, ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)
            print('data added')
            msgstr = """Dear user,\nThis mail is to inform you that you have updated your account details\n
            so now your updated details are:
            Account Number: %s
            Name = %s
            DOB = %s
            Email = %s
            Mobile NO = %s
            Gender = %s
            Addhar NO = %s
            Password = %s
            """ % (data['Account Number'],data['Name'], data['DOB'], data['Email'], data['Mobile Number'], data['Gender'], data['Aadhar Number'], data['Password'])
            SendEmail(data['Email'], 'Your Bank Details', msgstr)
            messagebox.showinfo("User Details", "Check your email for your Bank Details")
            LoginUser(2)
        else:
            messagebox.showwarning("OTP failed", "Please try again")
            print("Verififcation failed")
            return


root = tk.Tk()


Window_height = root.winfo_screenheight()
Window_width = root.winfo_screenwidth()
Geometry = str(Window_width) + "x" + str(Window_height) + "+-10+0"


root.geometry(Geometry)
root.title('BANK MANAGEMENT SYSTEM')


im = Image.open('BG.png')
im = im.resize((Window_width, Window_height), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(im)
ph1 = PhotoImage(file="th.png")
ph2 = PhotoImage(file="deposit-removebg-preview.png")
ph3 = PhotoImage(file="checkbalance1-removebg-preview.png")
ph4 = PhotoImage(file="withdraw-removebg-preview.png")
ph5 = tk.PhotoImage(file='signup-removebg-preview.png')
ph6 = tk.PhotoImage(file='login-removebg-preview.png')
ph7 = tk.PhotoImage(file='b2.png')
ph8 = PhotoImage(file="update-removebg-preview.png")
ph9 = tk.PhotoImage(file='pbb.png')



def destroy(n):
    global frame1, frame2, frame3, frame4
    if n == 0:
        return
    elif n == 1:
        frame1.destroy()
    elif n == 2:
        frame2.destroy()
    elif n == 3:
        frame3.destroy()
    elif n == 4:
        frame4.destroy()



def userFrame(n):
    global frame1, frame2, frame3, frame4
    destroy(n)
    frame1 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame1.pack(pady=5, padx=5)

    mainMenuLabel = tk.Label(frame1, text="WELCOME TO BANK MANAGEMENT SYSTEM", padx=15,
                             pady=15, bg="#00bbf0", fg="#00204a", font=("Tw Cen MT Condensed Extra Bold", 50))
    mainMenuLabel.place(y=-370, relx=0.5, rely=0.5, anchor='center')

    oldUserButton = tk.Button(frame1,  image=ph6, text="Click here to login to old account", command=lambda: LoginUser(1),
                              bg="#00bbf0", fg="white", font=("Modern No.", 11, "bold"))
    oldUserButton.place(y=50, x=300, relx=0.5, rely=0.5, anchor='center')

    newUserButton = tk.Button(frame1, text="Click here to create a new account", command=createAccount, font=(
        "Modern No.", 11, "bold"), bg="#00bbf0", fg="white", image=ph5)
    newUserButton.place(y=50, x=-300, relx=0.5, rely=0.5, anchor='center')



def EditInfo():
    print("Updating Info")
    global nameEntryBox, DOBEntryBox, emailEntryBox, mobileEntryBox, addharEntryBox, gen, newPassEntrybox
    global ind,acc,Name,DOB,Email,mobileNO,gender,aadharNO,currentBal,passWord
    global amt, frame4, acc

    frame4 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame4.pack(pady=5, padx=5)

    # This will destroy the Exisitng frame3 which was for MAIN screen
    frame3.destroy()

    # Creating the Title of the update account details window
    TitleLabel = tk.Label(frame4,text=f"UPDATE WINDOW FOR USER {acc}",
                          width=100, height=3, font=("BankGothic Md BT ", 20), bg="#264e70", fg="#ffebd3")
    TitleLabel.place(rely=0.45, relx=0.5, y=-324, anchor=CENTER)

    # First Entry box to Enter Name
    nameEntryBox = Entry(frame4, font=("BankGothic Md BT", 15, "bold"))
    nameEntryBox.place(y=-250, x=50, relx=0.5, rely=0.5,
                       anchor=CENTER, width=500, height=30)
    nameEntryBox.insert(0, Name)

    # Name Input Label
    nameInputLabel = Label(frame4, text="NAME :", padx=10, pady=5, bg="#00bbf0", fg="#cae8ff",
                           font=("Tw Cen MT Condensed Extra Bold", 15))
    nameInputLabel.place(y=-250, x=-250, relx=0.5, rely=0.5, anchor=CENTER)

    # DOB Entry box to Enter Name
    DOBEntryBox = Entry(frame4, font=("BankGothic Md BT", 15, "bold"))
    DOBEntryBox.place(y=-200, x=50, relx=0.5, rely=0.5,
                      anchor=CENTER, width=500, height=30)
    DOBEntryBox.insert(0, DOB)

    # DOB Input Label
    DOBInputLabel = Label(frame4, text="DOB :", padx=16, pady=5, bg="#00bbf0", fg="#cae8ff",
                          font=("Tw Cen MT Condensed Extra Bold", 15))
    DOBInputLabel.place(y=-200, x=-250, relx=0.5, rely=0.5, anchor=CENTER)

    # Email Entry box to Enter Name
    emailEntryBox = Entry(frame4, font=("BankGothic Md BT", 15, "bold"))
    emailEntryBox.place(y=-150, x=50, relx=0.5, rely=0.5,
                        anchor=CENTER, width=500, height=30)
    emailEntryBox.insert(0, Email)

    # Email Input Label
    emailEntryLabel = Label(frame4, text="Email :", padx=10, pady=5, bg="#00bbf0", fg="#cae8ff",
                            font=("Tw Cen MT Condensed Extra Bold", 15))
    emailEntryLabel.place(y=-150, x=-250, relx=0.5, rely=0.5, anchor=CENTER)

    # MobileNo Entry box to Enter Name
    mobileEntryBox = Entry(frame4, font=("BankGothic Md BT", 15, "bold"))
    mobileEntryBox.place(y=-100, x=50, relx=0.5, rely=0.5,
                         anchor=CENTER, width=500, height=30)
    mobileEntryBox.insert(0, mobileNO)

    # MobileNo Input Label
    mobileEntryLabel = Label(frame4, text="MobileNo :", padx=14, pady=5, bg="#00bbf0", fg="#cae8ff",
                             font=("Tw Cen MT Condensed Extra Bold", 15))
    mobileEntryLabel.place(y=-100, x=-270, relx=0.5, rely=0.5, anchor=CENTER)

    # Gender radio button
    gen = StringVar(frame4)
    gen.set(gender)
    genderList = OptionMenu(frame4, gen, "Male", "Female", "Other")
    genderList.place(y=-50, x=-50, relx=0.5, rely=0.5,
                     anchor=CENTER, width=300, height=30)

    # Gender Input Label
    genderLabel = Label(frame4, text="Gender :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                        font=("Tw Cen MT Condensed Extra Bold", 15))
    genderLabel.place(y=-50, x=-250, relx=0.5, rely=0.5, anchor=CENTER)

    # aadharNO Entry box to Enter Name
    addharEntryBox = Entry(frame4, font=("BankGothic Md BT", 15, "bold"))
    addharEntryBox.place(y=0, x=50, relx=0.5, rely=0.5,
                         anchor=CENTER, width=500, height=30)
    addharEntryBox.insert(0, aadharNO)

    # aadharNO Input Label
    addharEntryLabel = Label(frame4, text="aadharNO :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                             font=("Tw Cen MT Condensed Extra Bold", 15))
    addharEntryLabel.place(y=0, x=-261, relx=0.5, rely=0.5, anchor=CENTER)

    # password making field
    newPassWordLabel = Label(frame4, text="password :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                             font=("Tw Cen MT Condensed Extra Bold", 15))
    newPassWordLabel.place(y=50, x=-261, relx=0.5, rely=0.5, anchor=CENTER)

    # password entry box
    newPassEntrybox = Entry(frame4, font=("BankGothic Md BT", 15, "bold"))
    newPassEntrybox.place(y=50, x=50, relx=0.5, rely=0.5,
                          anchor=CENTER, width=500, height=30)
    newPassEntrybox.insert(0, passWord)

    # Submit Button after completely adding in the data
    submitButton = Button(frame4, text="SUBMIT", font=("Tw Cen MT Condensed Extra Bold", 15),
                          padx=30, pady=10, width=7, height=1, command=UpdateInfo)
    submitButton.place(y=120, x=-133, relx=0.5, rely=0.5, anchor=CENTER)

    # Account deletion button
    deleteAccount = Button(frame4, text="DELETE", font=("Tw Cen MT Condensed Extra Bold", 15),
                           padx=30, pady=10, width=7, height=1, command=delAccount)
    deleteAccount.place(y=120, x=233, relx=0.5, rely=0.5, anchor=CENTER)

    # Back button
    RewindTimeButton = Button(frame4, text="BACK", command=lambda: mainWindow(4), image=ph7,
                              font=("Modern No.", 11, "bold"), bg="#00bbf0", fg="white")
    RewindTimeButton.place(height=100, width=100, relx=0.5,
                           rely=0.5, anchor=CENTER, x=390, y=300)

    # Resets the Value in the Entry boxes
    def Reset():
        nameEntryBox.delete(0, END)
        nameEntryBox.insert(0, Name)
        DOBEntryBox.delete(0, END)
        DOBEntryBox.insert(0, DOB)
        emailEntryBox.delete(0, END)
        emailEntryBox.insert(0, Email)
        mobileEntryBox.delete(0, END)
        mobileEntryBox.insert(0, mobileNO)
        gen.set(gender)
        addharEntryBox.delete(0, END)
        addharEntryBox.insert(0, aadharNO)
        newPassEntrybox.delete(0, END)
        newPassEntrybox.insert(0, passWord)
        return

    resetButton = Button(frame4, text="RESET", font=("Tw Cen MT Condensed Extra Bold", 15),
                         padx=30, pady=10, width=7, height=1, command=Reset)
    resetButton.place(y=120, x=50, relx=0.5, rely=0.5, anchor=CENTER)

    return



def delAccount():
    ask = messagebox.askokcancel(
        "Deleting Accout", "Are you sure you want to delete your account?")
    if (ask):
        print("Deleting Accout")
        global ind, acc
        # removes the users transaction history file
        os.remove(str(acc)+'-rec.txt')
        # removing everything from excel
        df = pd.read_excel(EXCEL_FILE)
        df.loc[ind, 'Name'] = ''
        df.loc[ind, 'DOB'] = ''
        df.loc[ind, 'Email'] = ''
        df.loc[ind, 'Mobile Number'] = 0
        df.loc[ind, 'Gender'] = ''
        df.loc[ind, 'Aadhar Number'] = ''
        df.loc[ind, 'Password'] = '-1'
        df.loc[ind, 'Account Number'] = '-1'
        df.loc[ind, 'Balance'] = ''
        df.to_excel(EXCEL_FILE, index=False)
        messagebox.showinfo("Deleted successfully",
                            "Account Successfully Removed")
        userFrame(4)
    return



def createAccount():
    print('in acc')
    global frame1, frame2, frame3, frame4
    global nameEntryBox, DOBEntryBox, emailEntryBox, mobileEntryBox, addharEntryBox, gen, newPassEntryBox, AccNO, openingBalBox

    frame1.destroy()

    frame2 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame2.pack(pady=5, padx=5)

    accountOpeningLabel = tk.Label(frame2, text="Welcome to BMS\n Please add the following details to continue",
                                   width=100, height=3, font=("BankGothic Md BT ", 20), bg="#264e70", fg="#ffebd3")
    accountOpeningLabel.place(y=-324, relx=0.5, rely=0.45, anchor=CENTER)

    # First Entry box to Enter Name and label
    nameEntryBox = tk.Entry(frame2, font=(
        "BankGothic Md BT", 15), border=0, bg="#00bbf0")
    nameEntryBox.place(y=-150, x=50, relx=0.5, rely=0.5,
                       anchor=CENTER, width=500, height=30)
    nameEntryBox.insert(0, "FirstName MiddleName LastName")
    nameEntryBox.bind('<FocusIn>', lambda e: nameEntryBox.delete(
        0, 'end') if (nameEntryBox.get() == 'FirstName MiddleName LastName' ) else None)
    nameEntryBox.bind('<FocusOut>', lambda e:  nameEntryBox.insert(
        0, 'FirstName MiddleName LastName') if (nameEntryBox.get() == '') else None )
    nameInputLabel = tk.Label(frame2, text="Name :", padx=10, pady=5,
                              bg="#00bbf0", fg="#cae8ff", font=("Tw Cen MT Condensed Extra Bold", 15))
    nameInputLabel.place(y=-150, x=-250, relx=0.5, rely=0.5, anchor=CENTER)
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(x=-200, y=-140,relx=0.5, rely=0.5)



    # DOB Entry box to Enter Name and label
    DOBEntryBox = tk.Entry(frame2, font=("BankGothic Md BT", 15),border=0, bg="#00bbf0")
    DOBEntryBox.place(y=-100, x=50, relx=0.5, rely=0.5,
                      anchor=CENTER, width=500, height=30)
    DOBEntryBox.insert(0, "DD/MM/YYYY")
    DOBEntryBox.bind('<FocusIn>', lambda e: DOBEntryBox.delete(0, 'end') if (
        DOBEntryBox.get() == 'DD/MM/YYYY') else None)
    DOBEntryBox.bind('<FocusOut>', lambda e:  DOBEntryBox.insert(
        0, 'DD/MM/YYYY') if (DOBEntryBox.get() == '') else DOBEntryBox.get())
    DOBInputLabel = tk.Label(frame2, text="DOB :", padx=16, pady=5,
                             bg="#00bbf0", fg="#cae8ff", font=("Tw Cen MT Condensed Extra Bold", 15))
    DOBInputLabel.place(y=-100, x=-250, relx=0.5, rely=0.5, anchor=CENTER)
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-200, y=-90, relx=0.5, rely=0.5)



    # Email Entry box to Enter Name
    emailEntryBox = tk.Entry(frame2, font=(
        "BankGothic Md BT", 15), border=0, bg="#00bbf0")
    emailEntryBox.place(y=-50, x=50, relx=0.5, rely=0.5,
                        anchor=CENTER, width=500, height=30)
    emailEntryBox.insert(0, "JohnDoe@mail.com")
    emailEntryBox.bind('<FocusIn>', lambda e: emailEntryBox.delete(0, 'end') if (
        emailEntryBox.get() == 'JohnDoe@mail.com') else None)
    emailEntryBox.bind('<FocusOut>', lambda e:  emailEntryBox.insert(
        0, 'JohnDoe@mail.com') if (emailEntryBox.get() == '') else emailEntryBox.get())
    # Email Input Label
    emailEntryLabel = tk.Label(frame2, text="Email :", padx=10, pady=5,
                               bg="#00bbf0", fg="#cae8ff", font=("Tw Cen MT Condensed Extra Bold", 15))
    emailEntryLabel.place(y=-50, 
                          x=-250, relx=0.5, rely=0.5, anchor=CENTER)
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-200, y=-40, relx=0.5, rely=0.5)



    # MobileNo Entry box to Enter Name
    mobileEntryBox = tk.Entry(frame2, font=(
        "BankGothic Md BT", 15), border=0, bg="#00bbf0")
    mobileEntryBox.place(y=0, x=50, relx=0.5, rely=0.5,
                         anchor=CENTER, width=500, height=30)
    mobileEntryBox.insert(0, "XXXXXXXXXX")
    mobileEntryBox.bind('<FocusIn>', lambda e: mobileEntryBox.delete(0, 'end') if (
        mobileEntryBox.get() == 'XXXXXXXXXX') else None)
    mobileEntryBox.bind('<FocusOut>', lambda e:  mobileEntryBox.insert(
        0, 'XXXXXXXXXX') if (mobileEntryBox.get() == '') else mobileEntryBox.get())
    # MobileNo Input Label
    mobileEntryLabel = tk.Label(frame2, text="MobileNo :", padx=14, pady=5, bg="#00bbf0", fg="#cae8ff",
                                font=("Tw Cen MT Condensed Extra Bold", 15))
    mobileEntryLabel.place(y=0, x=-270, relx=0.5, rely=0.5, anchor=CENTER)
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-200, y=10, relx=0.5, rely=0.5)



    # Gender radio button and label
    gen = StringVar()
    gen.set("Gender")
    genderList = OptionMenu(frame2, gen, "Male", "Female", "Other")
    genderList.place(y=50, x=-50, relx=0.5, rely=0.5,
                     anchor=CENTER, width=300, height=30)
    genderLabel = Label(frame2, text="Gender :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                        font=("Tw Cen MT Condensed Extra Bold", 15))
    genderLabel.place(y=50, x=-250, relx=0.5, rely=0.5, anchor=CENTER)



    # aadharNO Entry box to Enter Name and label
    addharEntryBox = Entry(frame2, font=(
        "BankGothic Md BT", 15), border=0, bg="#00bbf0")
    addharEntryBox.place(y=100, x=50, relx=0.5, rely=0.5,
                         anchor=CENTER, width=500, height=30)
    addharEntryBox.insert(0, "XXXX XXXX XXXX")
    addharEntryBox.bind('<FocusIn>', lambda e: addharEntryBox.delete(0, 'end') if (
        addharEntryBox.get() == 'XXXX XXXX XXXX') else None)
    addharEntryBox.bind('<FocusOut>', lambda e:  addharEntryBox.insert(
        0, 'XXXX XXXX XXXX') if (addharEntryBox.get() == '') else addharEntryBox.get())
    addharEntryLabel = Label(frame2, text="AadharNO :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                             font=("Tw Cen MT Condensed Extra Bold", 15))
    addharEntryLabel.place(y=100, x=-261, relx=0.5, rely=0.5, anchor=CENTER)
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-200, y=110, relx=0.5, rely=0.5)



    # password making field and entry box
    newPassWordLabel = Label(frame2, text="Password :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                             font=("Tw Cen MT Condensed Extra Bold", 15))
    newPassWordLabel.place(y=150, x=-261, relx=0.5, rely=0.5, anchor=CENTER)
    newPassEntryBox = Entry(
        frame2, show="*", font=("BankGothic Md BT", 15), border=0, bg="#00bbf0")
    newPassEntryBox.place(y=150, x=50, relx=0.5, rely=0.5, 
                          anchor=CENTER, width=500, height=30)
    newPassEntryBox.insert(0, "min 8 digit password")
    newPassEntryBox.bind(
        '<FocusIn>', lambda e: newPassEntryBox.delete(0, 'end')if (newPassEntryBox.get() == 'min 8 digit password') else None)
    newPassEntryBox.bind('<FocusOut>', lambda e:  newPassEntryBox.insert(
        0, 'min 8 digit password') if (newPassEntryBox.get() == '') else newPassEntryBox.get())
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-200, y=160, relx=0.5, rely=0.5)



    # opening credit entry box and label
    openingBalBox = Entry(frame2, font=(
        "BankGothic Md BT", 15), border=0, bg="#00bbf0")
    openingBalBox.place(y=200, x=50, relx=0.5, rely=0.5,
                        anchor=CENTER, width=500, height=30)
    openingBalBox.insert(0, "deposit min Rs 2500")
    openingBalBox.bind('<FocusIn>', lambda e: openingBalBox.delete(0, 'end') if (
        openingBalBox.get() == 'deposit min Rs 2500') else None)
    openingBalBox.bind('<FocusOut>', lambda e:  openingBalBox.insert(
        0, 'deposit min Rs 2500') if (openingBalBox.get() == '') else openingBalBox.get())
    openingBalLabel = Label(frame2, text="Opening Credit :", padx=5, pady=5, bg="#00bbf0", fg="#cae8ff",
                            font=("Tw Cen MT Condensed Extra Bold", 15))
    openingBalLabel.place(y=200, x=-280, relx=0.5, rely=0.5, anchor=CENTER)
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-200, y=210, relx=0.5, rely=0.5)

    # Accout number to be created randoml
    AccNO = random.randint(10 ** 12, (10 ** 13) - 1)

    # Submit Button after completely adding in the data
    submitButton = tk.Button(frame2, text="SUBMIT", font=("Tw Cen MT Condensed Extra Bold", 15),
                             padx=30, pady=10, width=7, height=1, command=lambda: Verify(1))
    submitButton.place(y=270, x=-115, relx=0.5, rely=0.5, anchor=CENTER)

    # Rewind Button
    backButton = tk.Button(frame2, text="BACK", image=ph7, width=5, height=52,
                           font=("Modern No.", 11), bg="#00bbf0",  fg="white", command=lambda: userFrame(2))
    backButton.place(height=100, width=100, relx=0.5,
                     rely=0.5, anchor=CENTER, x=480, y=300)



    def Reset():
        nameEntryBox.delete(0, END)
        nameEntryBox.insert(0, 'FirstName MiddleName LastName')
        DOBEntryBox.delete(0, END)
        DOBEntryBox.insert(0, 'DD/MM/YYYY')
        emailEntryBox.delete(0, END)
        emailEntryBox.insert(0, 'JohnDoe@mail.com')
        mobileEntryBox.delete(0, END)
        mobileEntryBox.insert(0, 'XXXXXXXXXX')
        gen.set('Gender')
        addharEntryBox.delete(0, END)
        addharEntryBox.insert(0, 'XXXX XXXX XXXX')
        newPassEntryBox.delete(0, END)
        newPassEntryBox.insert(0, 'min 8 digit password')
        openingBalBox.delete(0, END)
        openingBalBox.insert(0, 'deposit min Rs 2500')
        return



    resetButton = Button(frame2, text="RESET", font=("Tw Cen MT Condensed Extra Bold", 15),
                         padx=30, pady=10, width=7, height=1, command=Reset)
    resetButton.place(y=270, x=50, relx=0.5, rely=0.5, anchor=CENTER)



def Verify(n):
    global nameEntryBox, DOBEntryBox, emailEntryBox, mobileEntryBox, addharEntryBox, gen, newPassEntryBox, AccNO, openingBalBox
    if (n == 1):
        name_user = nameEntryBox.get()
        dob = DOBEntryBox.get()
        e = emailEntryBox.get()
        mob = mobileEntryBox.get()
        adr = addharEntryBox.get()
        g = gen.get()
        pswd = newPassEntryBox.get()
        bal = openingBalBox.get()
        try:
            first, middle, last = name_user.split(' ')
        except:
            messagebox.showerror(
                "Error occured ", "Enter correct formatwise name")
            return

        try:
            curr = int(mob)
        except:
            messagebox.showerror("Error occured ", "Enter correct MobileNO")
            return

        try:
            curr = int(bal)
        except:
            messagebox.showerror("Error occured ", "Enter deposit in Numbers")
            return

        if (len(mob) != 10):
            messagebox.showerror(
                "Error occured ", "Mobile number number length is incorrect")
            return

        if (len(pswd) < 8):
            messagebox.showerror(
                "Error occured ", "Password number length is incorrect")
            return

        if (len(str(adr)) != 14):
            messagebox.showerror(
                "Error occured ", "Addhar number number length is incorrect")
            return

        if (int(bal) < 2500):
            messagebox.showerror(
                "Error occured ", "Minimum depoit of 2500Rs is required")
            return
        obj = User(first, middle, last, dob, e, mob, g, adr, AccNO, pswd, bal)
    elif (n == 2):
        global AccNOEntryBox, passWordEntrybox, acc, pas, ind
        acc = AccNOEntryBox.get()
        pas = passWordEntrybox.get()
        df = pd.read_excel(EXCEL_FILE)

        ind = (df.loc[df['Account Number'] == int(acc)]).index[0]

        print(ind)
        acpa = df[['Account Number', 'Password']].set_index(
            'Account Number').to_dict()['Password']
        if int(acc) in acpa and str(acpa[int(acc)]) == pas:
            print(acpa, 'Verified')
        else:
            messagebox.showerror(
                "Error occured ", "Account Number/Password incorrect")
            return
        mainWindow(2)



def loadData():
    global ind,acc,Name,DOB,Email,mobileNO,gender,aadharNO,currentBal,passWord
    print('in Load')
    df = pd.read_excel(EXCEL_FILE)
    Name = str(df.loc[ind, 'Name'])
    DOB = str(df.loc[ind, 'DOB'])[:10] 
    Email = str(df.loc[ind, 'Email'])
    mobileNO = int(df.loc[ind, 'Mobile Number'])
    gender = str(df.loc[ind, 'Gender'])
    aadharNO = str(df.loc[ind, 'Aadhar Number'])
    currentBal = float(df.loc[ind, 'Balance'])
    passWord = str(df.loc[ind, 'Password'])
    print(f'name={Name},DOB={DOB},Email={Email},Gender={gender},mob={mobileNO},addhar={aadharNO},bal={currentBal},pass={passWord}')



def UpdateInfo():
    print("Updating old users data in excel")
    global Name, DOB, Email, mobileNO, gender, aadharNO, passWord
    # Reading the Excel file
    df = pd.read_excel(EXCEL_FILE)
    DOB = DOBEntryBox.get()
    Email = emailEntryBox.get()
    Name = nameEntryBox.get()
    mobileNO = mobileEntryBox.get()
    gender = gen.get()
    aadharNO = addharEntryBox.get()
    passWord = newPassEntrybox.get()
    print(ind,Name,DOB,Email,mobileNO,gender,aadharNO,passWord)
    df.loc[ind,'Name'] = Name
    df.loc[ind, 'DOB'] = DOB
    df.loc[ind, 'Email'] = Email
    df.loc[ind, 'Mobile Number'] = mobileNO
    df.loc[ind, 'Gender'] = gender
    df.loc[ind, 'Aadhar Number'] = aadharNO
    df.loc[ind, 'Password'] = passWord

    # writing to the Excel file
    df.to_excel(EXCEL_FILE, index=False)

    # updating the variables
    loadData()

    # Sending user an email that his account was updated
    msgstr = """Dear user,\nThis mail is to inform you that you have updated your account details\n
    so now your updated details are:
    Name = %s
    DOB = %s
    Email = %s
    Mobile NO = %s
    Gender = %s
    Addhar NO = %s
    Password = %s
    """ % (Name, DOB, Email, mobileNO, gender, aadharNO, passWord)
    SendEmail(Email,'Successfully Edited your Info',msgstr)

    messagebox.showinfo(
        "InfoUpdated", "Your account details have been updated please check your email")
    mainWindow(4)
    return



def mainWindow(n):
    print("Main Transaction Window")
    global frame1, frame2, frame3, frame4
    global Name,nameEntryBox, DOBEntryBox, emailEntryBox, mobileEntryBox, addharEntryBox, gen, newPassEntryBox, AccNO, openingBalBox
    destroy(n)
    loadData()

    frame3 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame3.pack(pady=5, padx=5)

    userLabel = Label(frame3,width=Window_width, height=2, font=("BankGothic Md BT ", 15), bg="#264e70", fg="#fff")
    userLabel.place(rely=0.42, relx=0.5, y=-324,anchor=CENTER)
    userName = Label(frame3,text=Name, width=20, height=1, font=(
        "BankGothic Md BT ", 15), bg="#264e70", fg="#ffebd3")
    userName.place(rely=0.422, relx=0.5,x=590, y=-324, anchor=CENTER)

    LogOutButton = Button(
        frame3, image=ph9, command=logout, bg='#fff')
    LogOutButton.place(anchor=CENTER, relx=0.5, rely=0.422, x=720, y=-324)
    
    # transaction button
    transactButton = Button(frame3, image=ph1,command=transactionHistory,bg='#00bbf0')
    transactButton.place(anchor=CENTER, relx=0.5, rely=0.5, x=510, y=50)
    transhistLabel = Label(frame3, text='Transaction\nHistory', width=10, height=2, font=(
        "BankGothic Md BT ", 20), bg="#00bbf0", fg="#fff")
    transhistLabel.place(rely=0.5, relx=0.5, x=320, y=50, anchor=CENTER)


    # deposit button
    depositButton = Button(frame3, image=ph2, command=deposit, bg='#00bbf0')
    depositButton.place(anchor=CENTER, relx=0.5, rely=0.5, x=-520, y=50)
    depositLabel = Label(frame3, text='Deposit', width=10, height=2, font=(
        "BankGothic Md BT ", 20), bg="#00bbf0", fg="#fff")
    depositLabel.place(rely=0.5, relx=0.5, x=-350, y=50, anchor=CENTER)

    # withdraw button
    withdrawButton = Button(frame3, image=ph4, command=withdraw, bg='#00bbf0')
    withdrawButton.place(anchor=CENTER, relx=0.5, rely=0.5, x=-520, y=-200)
    withdrawLabel = Label(frame3, text='Withdraw', width=10, height=2, font=(
        "BankGothic Md BT ", 20), bg="#00bbf0", fg="#fff")
    withdrawLabel.place(rely=0.5, relx=0.5, x=-350, y=-200, anchor=CENTER)

    # show account balance button
    accountBalButton = Button(
        frame3, image=ph3, command=popupCurrentBal, bg='#00bbf0')
    accountBalButton.place(anchor=CENTER, relx=0.5, rely=0.5, x=510, y=-200)
    accbalLabel = Label(frame3, text='Available\nBalance', width=10, height=2, font=(
        "BankGothic Md BT ", 20), bg="#00bbf0", fg="#fff")
    accbalLabel.place(rely=0.5, relx=0.5, x=320, y=-200, anchor=CENTER)

    # update the users details
    editInfoButton = Button(frame3, text="Update Information",
                            image=ph8, fg="#2596be", command=EditInfo, bg='#00bbf0')
    editInfoButton.place(anchor=CENTER, relx=0.5, rely=0.5,
                         y=200, width=300, height=100)

    return



def logout():
    print('in logout')
    ask = messagebox.askokcancel("Warning!", "Are you sure you want to log out?")
    if (ask):
        userFrame(3)
    else:
        return



def SendEmail(Email, subject, msgstr):
    print("Emailing")
    msg = MIMEText(msgstr)
    msg['Subject'] = subject
    msg['From'] = "pythonemailtestservice@gmail.com"
    msg['To'] = Email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("pythonemailtestservice@gmail.com", "tzleaaknhfstkngz")
    s.sendmail("pythonemailtestservice@gmail.com", Email, msg.as_string())
    s.quit()
    print("Done Email")
    return



def LoginUser(n):
    print("Welcome OLd User")
    global frame1, frame2, frame3, frame4
    global nameEntryBox, DOBEntryBox, emailEntryBox, mobileEntryBox, addharEntryBox, gen, newPassEntryBox, AccNO, openingBalBox
    # This will destroy the Exisitng frame1 which was for loading screen
    destroy(n)
    frame2 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame2.pack(pady=5, padx=5)
    global AccNOEntryBox, passWordEntrybox

    # Banner to welcome The old user
    TitleLabel = Label(frame2,
                       text="Welcome Again !!\n Please enter your details ",
                       width=100, height=3, font=("BankGothic Md BT ", 20), bg="#264e70", fg="#ffebd3")
    TitleLabel.place(rely=0.45, relx=0.5, y=-324, anchor=CENTER)

    # Entry field to enter ID
    AccNOEntryBox = Entry(frame2, font=(
        "BankGothic Md BT", 20), border=0, bg="#00bbf0")
    AccNOEntryBox.place(y=-60, x=25, relx=0.5, rely=0.5,
                        anchor=CENTER, width=400, height=50)
    AccNOEntryBox.insert(0, "Account Number")
    AccNOEntryBox.bind('<FocusIn>', lambda e: AccNOEntryBox.delete(0, 'end') if (
        AccNOEntryBox.get() == 'Account Number') else None)
    AccNOEntryBox.bind('<FocusOut>', lambda e:  AccNOEntryBox.insert(
        0, 'Account Number') if (AccNOEntryBox.get() == '') else AccNOEntryBox.get())
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
    x=-176, y=-47, relx=0.5, rely=0.5)

    passWordEntrybox = Entry(frame2, font=(
        "BankGothic Md BT", 20), border=0, bg="#00bbf0",show="*")
    passWordEntrybox.place(y=10, x=25, relx=0.5, rely=0.5,
                           anchor=CENTER, width=400, height=50)
    passWordEntrybox.insert(0, "Enter your Password")
    passWordEntrybox.bind('<FocusIn>', lambda e: passWordEntrybox.delete(0, 'end') if (
        passWordEntrybox.get() == 'Enter your Password') else None)
    passWordEntrybox.bind('<FocusOut>', lambda e:  passWordEntrybox.insert(
        0, 'Enter your Password') if (passWordEntrybox.get() == '') else passWordEntrybox.get())
    tk.LabelFrame(frame2, width=330, height=3, bg="#000").place(
        x=-176, y=24, relx=0.5, rely=0.5)


    # Submit button to get the data and verify it
    submitButton = Button(frame2, text="SUBMIT", font=("Tw Cen MT Condensed Extra Bold", 15),
                          padx=30, pady=10, width=7, height=1, command=lambda: Verify(2))
    submitButton.place(y=80, x=-90, relx=0.5, rely=0.5, anchor=CENTER)

    RewindTimeButton = Button(frame2, text="<--", image=ph7, command=lambda: userFrame(2),
                              padx=300, pady=100, width=7, height=1, font=("Modern No.", 10), fg="#00bbf0", bg="#00bbf0")
    RewindTimeButton.place(height=100, width=100, relx=0.5,
                           rely=0.5, anchor=CENTER, x=480, y=300)

    def Reset():
        AccNOEntryBox.delete(0, END)
        AccNOEntryBox.insert(0, "Account Number")
        passWordEntrybox.delete(0, END)
        passWordEntrybox.insert(0, "Enter your Password")
        return

    resetButton = Button(frame2, text="RESET", font=("Tw Cen MT Condensed Extra Bold", 15),
                         padx=30, pady=10, width=7, height=1, command=Reset)
    resetButton.place(y=80, x=70, relx=0.5, rely=0.5, anchor=CENTER)
    return



def popupCurrentBal():
    print("Showing Current Balance")
    global acc
    df = pd.read_excel(EXCEL_FILE)
    acc_bal = df[['Account Number', 'Balance']].set_index(
        'Account Number').to_dict()['Balance']
    acc_name = df[['Account Number',  'Name']].set_index(
        'Account Number').to_dict()['Name']
    messagebox.showinfo("Current Account Balance", "%s's Current Balance :%s " % (acc_name[int(acc)],
                                                                                  acc_bal[int(acc)]))
    return



def withdraw():
    print("Withdraw windows")
    destroy(3)
    global amt,frame4
    frame4 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame4.pack(pady=5, padx=5)
    TitleLabel = tk.Label(frame4,
                       text="WITHDRAW WINDOW",
                       width=100, height=3, font=("BankGothic Md BT ", 20), bg="#264e70", fg="#ffebd3")
    TitleLabel.place(rely=0.45, relx=0.5, y=-324, anchor=CENTER)

    amountLabel = Label(frame4, text="Please Enter the amount you want to withdraw:",
                        width=100, height=2, font=("BankGothic Md BT ", 20), bg="#00bbf0", fg="#ffebd3")
    amountLabel.place(rely=0.5, relx=0.5, y=-100, anchor=CENTER)

    amt = Entry(frame4, font=("BankGothic Md BT ", 20, "bold"))
    amt.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20, width=400, height=50)

    WithdrawButton = tk.Button(frame4, font=("BankGothic Md BT ", 15, "bold"),
                               text="Withdraw", command=lambda: update(1))
    WithdrawButton.place(relx=0.5, rely=0.5, anchor=CENTER,
                         y=100, width=100, height=50)

    RewindTimeButton = Button(frame4, text="BACK", image=ph7, command=lambda: mainWindow(4), height=100,
                              width=100, font=("Modern No.", 11, "bold"), bg="#00bbf0", fg="white")
    RewindTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER, x=480, y=300)



def deposit():
    print("deposit windows")
    destroy(3)
    global amt, frame4
    frame4 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame4.pack(pady=5, padx=5)
    TitleLabel = Label(frame4,
                       text="Deposit Window",
                       width=100, height=3, font=("BankGothic Md BT ", 20), bg="#264e70", fg="#ffebd3")
    TitleLabel.place(rely=0.45, relx=0.5, y=-324, anchor=CENTER)

    amt = Entry(frame4, font=("BankGothic Md BT ", 20, "bold"))
    amt.place(relx=0.5, rely=0.5, anchor=CENTER, y=-20, width=400, height=50)

    amountLabel = Label(frame4,text="Please Enter the amount you want to deposit:",
                        width=100, height=2, font=("BankGothic Md BT ", 20), bg="#00bbf0", fg="#ffebd3")
    amountLabel.place(rely=0.5, relx=0.5, y=-100, anchor=CENTER)

    depositButton = tk.Button(frame4, font=("BankGothic Md BT ", 15, "bold"),
                               text="Deposit", command=lambda:update(2))
    depositButton.place(relx=0.5, rely=0.5, anchor=CENTER,
                         y=100, width=100, height=50)

    RewindTimeButton = Button(frame4, text="BACK", image=ph7, command=lambda: mainWindow(4),height=100,
                              width=100, font=("Modern No.", 11, "bold"), bg="#00bbf0", fg="white")
    RewindTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER, x=480, y=300)



def update(n):
    global amt,bal,frame4
    global ind, acc, Name, DOB, Email, mobileNO, gender, aadharNO, currentBal, passWord
    print(float(amt.get()))
    try:
        amti = float(amt.get())
    except:
        messagebox.showerror("ValueError", "Please Enter correct amount")
        amt.delete(0, END)
        return
    amt.delete(0, END)
    print(currentBal)
    if (n == 1 and amti > currentBal or currentBal < 0):
            messagebox.showerror("MoneyIssues", "you are Broke")
            return
    elif(n==1):
        currentBal -= amti
        print("Amount subtracted", amti, currentBal, ind)
    if (n == 2):
        currentBal += amti
        print("Amount added", amti, currentBal, ind)
    df = pd.read_excel(EXCEL_FILE)
    df.loc[ind, 'Balance'] = currentBal
    print('\nbal in excel\n',df.loc[ind, 'Balance'])
    df.to_excel(EXCEL_FILE, index=False)
    txt = str(acc) + "-rec.txt"
    with open(txt,'a+') as f:
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
        if (n == 2):
            f.write(
                str(ind_time + "      " + str(amti) + "      " + str(currentBal) + "\n"))
        elif (n == 1):
            f.write(
                str(ind_time + "      " + "-" + str(amti) + "      " + str(currentBal) + "\n"))
    engine = pyttsx3.init()
    if (n == 2):
        engine.say(str(amti) + "Amount Deposited Successfully")
    elif (n == 1):
        engine.say(str(amti) + "Amount Withdrawed Successfully")
    engine.runAndWait()



def transactionHistory():
    print("Displaying transaction history")
    destroy(3)
    global amt, frame4,acc,Email,currentBal
    frame4 = tk.LabelFrame(
        root, bg="#00bbf0", width=Window_width, height=Window_height)
    frame4.pack(pady=5, padx=5)
    TitleLabel = tk.Label(frame4, text="TRANSACTION HISTORY OF USER : %s" % (acc),
                                   width=100, height=3, font=("BankGothic Md BT ", 20), bg="#264e70", fg="#ffebd3")
    TitleLabel.place(y=-324, relx=0.5, rely=0.45, anchor=CENTER)
    
    creditdebitLabel = tk.Label(frame4, text="Date             Credit/Debit       Balance",
                                width=100, height=3, font=("BankGothic Md BT ", 15), bg="#00bbf0", fg="#ffebd3")
    creditdebitLabel.place(x=-310,y=-204, relx=0.5, rely=0.5, anchor=CENTER)

    listOfTransactions = Listbox(
        frame4, width=100, height=15, font=("Modern No.", 15))
    scrollbar = Scrollbar(frame4)

    scrollbar.place(anchor=E)
    listOfTransactions.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listOfTransactions.yview)

    msgstr = 'Dear user your transaction history is :\n'
    listOfTransactions.place(relx=0.5, rely=0.5, anchor=CENTER)
    try:
        with open(str(acc) + "-rec.txt", 'r') as f:
            for line in f:
                msgstr += (line + "\n")
                listOfTransactions.insert(END, line)
    except:
        listOfTransactions.insert(END,f'Initially deposited money:{currentBal}')
    TransactMail = Button(frame4, text="MailTransactionHistory", command=lambda: SendEmail(Email,'Transaction History',msgstr),
                          font=("Modern No.", 11, "bold"))
    TransactMail.place(rely=0.5, relx=0.5, anchor=CENTER, x=-468, y=300)

    RewindTimeButton = Button(frame4, text="BACK", image=ph7, command=lambda: mainWindow(4),height=100,
                              font=("Modern No.", 11, "bold"), bg="#00bbf0", fg="white",width=100)
    RewindTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER, x=480, y=300)
    return



print(Window_height, Window_width, Geometry)
userFrame(0)
root.mainloop()
