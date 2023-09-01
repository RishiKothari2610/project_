# # name = self.first + ' ' + self.middle + ' ' + self.last
import openpyxl
import pandas as pd

# # data = {
# #     'Account Number': 8,
# #     'Password':'1234567890',
# #     'Name': 'joe',
# #     'DOB': '08/08/2003',
# #     'Email': '@gmail.com',
# #     'Mobile Number': '8200751854',
# #     'Gender': 'male',
# #     'Aadhar Number': '1001',
# #     'Balance': '2500'
# # }
# # df = pd.read_excel('BankDB.xlsx', engine='openpyxl')
# # df = df.append(data, ignore_index=True)
# # df.to_excel('BankDB.xlsx', index=False)

# # print(df)


# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# # Create a list of options for the OptionMenu
# options = ["Option 1", "Option 2", "Option 3"]

# # Create a StringVar object to hold the selected value
# selected_option = tk.StringVar()

# # Set the initial value of the StringVar
# selected_option.set(options[0])

# # Create the OptionMenu widget
# gen = tk.StringVar()
# gen.set("Gender")
# genderList = tk.OptionMenu(root,gen, "Male", "Female", "Other")
# genderList.place(y=50, x=-50, relx=0.5, rely=0.5,
#                  anchor='center', width=300, height=30)
# genderLabel = tk.Label(root,text="Gender :", padx=5, pady=5, bg="red", fg="#cae8ff",
#                     font=("Tw Cen MT Condensed Extra Bold", 15))
# genderLabel.place(y=50, x=-250, relx=0.5, rely=0.5, anchor='center')

# # Function to extract the selected value


# def extract_value():
#     value = gen.get()
#     print(value)


# # Create a button to extract the selected value
# button = tk.Button(root, text="Extract Value", command=extract_value)
# button.pack()
# import pyttsx3


# # root.mainloop()
# engine = pyttsx3.init()
# if True:
#     engine.say(str(40000) + "Amount Deposited Successfully")
# elif True:
#     engine.say(str(amti) + "Amount Withdrawed Successfully")
# engine.runAndWait()


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # 1 is the index of the female voice
# engine.setProperty('rate', 150)  # 150 words per minute
# engine.say("Hello, how are you?")
# engine.runAndWait()
import pandas as pd
from pandas import *
# def popupCurrentBal():
#     print("Showing Current Balance")
#     global firstName, lastName, middleName
#     firstName ='ya'
#     lastName ='p'
#     middleName ='d'
#     AccNO = 6790572504541
#     # EXCEL_FILE = path+'BMS.xlsx'
#     df = pd.read_excel('BankDB.xlsx')
#     # for i in range(0, len(df)):
#     #     if (str(AccNO) == str(df.loc[i, 'Account Number'])):
#     #         ii = i
#     # print(df)
#     # df = pd.read_excel(EXCEL_FILE)
#     # df = df
#     acpa = df[['Account Number', 'Password','Balance']].set_index('Account Number').to_dict()
#     ac = df[['Account Number', 'Password']].to_dict()['Account Number']
#     print(acpa,ac)
#     # if 
#     print("Current Account Balance", "%s's Balance : %s" % (
#         (firstName+' ' + middleName+' ' + lastName), df.loc[1, 'Balance']))
#     return


# def popupCurrentBal():
#     print("Showing Current Balance")
#     global firstName, lastName, middleName, AccNO
#     firstName = 'ya'
#     lastName ='p'
#     middleName ='d'
#     AccNO = 9421666385794

#     # EXCEL_FILE = path+'BMS.xlsx'
#     df = pd.read_excel('BankDB.xlsx')
#     acpa = df[['Account Number', 'Balance']].set_index(
#         'Account Number').to_dict()['Balance']
#     # acpa[AccNO]=6000
    
#     print("Current Account Balance", "%s's Balance : %s" % (
#         (firstName+' ' + middleName+' ' + lastName), acpa[AccNO]))
#     return
# popupCurrentBal()

import pandas as pd

# Read the Excel file into a Pandas dataframe
df = pd.read_excel('BankDB.xlsx')

# Specify the account number you want to access
account_number = 3270527940446

# Use the .loc[] function to select rows with the specified account number
a1= (df.loc[df['Account Number'] == account_number]).index[0]
a2 = str(df.loc[a1,'Email'])
a3 = str(df.loc[df['Account Number'] == account_number, 'Email'])
a4 = str(df.loc[df['Account Number'] == account_number, 'Name'])
a5 = str(df.loc[df['Account Number'] == account_number, 'Password'])


# Print the account data
# print(type(account_data))
# a1 = int(a1)
print(a1)
# print(a2)

# print(type(a2))
# print(type(a3))
# print(type(a4))
# print(type(a5))
# print(a2[5])
# print(a3[0])
# print(a4[0])
# print(a5[0])
