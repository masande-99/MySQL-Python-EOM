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



def verify():
    users = user.get()
    passs = passw.get()
    sql ="select * from Login where Username = %s and Password + %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

def failed():
     messagebox.showinfo("Failed loggging  in")
def logged():
    messagebox.showinfo("You have succesfully loggged in")

    root.destroy()

username = Label (root, text="Enter username")
username.pack()
user = Entry(root, width=45)
user.pack()

password = Label (root ,text="Enter your password")
password.pack()
passw = Entry(root, width=45)
passw.pack()

lgnbtn = Button(root , text="Submit")
lgnbtn.pack()

rgstbtn = Button(root, text="Register", command=verify)
rgstbtn.pack()



root.mainloop()
