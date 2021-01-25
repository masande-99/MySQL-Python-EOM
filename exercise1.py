import mysql.connector
from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
mydb=mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='hospital', host='127.0.0.1', auth_plugin='mysql_native_password')
mycursor=mydb.cursor()


root = Tk()
root.title("Login")
root.geometry('450x500')

global myresult


username = Label (root, text="Enter username")
username.pack()
user = Entry(root, width=45)
user.pack()

password = Label (root ,text="Enter your password")
password.pack()
passw = Entry(root, width=45)
passw.pack(ipady=40)

lgnbtn = Button(root , text="Submit")
lgnbtn.pack()

rgstbtn = Button(root, text="Register")
rgstbtn.pack()
def get_info():

    mydb = mysql.connector.connect(
      host="localhost",
      user="lifechoices",
      password="@Lifechoices1234",
      database="lifechoicesonline"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM users")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)




get_info()


root.mainloop()
