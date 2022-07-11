from tkinter import *
from tkinter import messagebox
import mysql.connector

from register import register_fun
from login import login_fun


root = Tk()
root.title("Cafe System Managment")
root.geometry("380x300")

# Create a mysql instant and connect it (will add database later when create it)
mydb = mysql.connector.connect(
                  host = "127.0.0.1",
                  user = "root",
                  passwd = "jmjmaaskull",
                  database = "cms")

# Create cursor object
cursor = mydb.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS cms")

"""
# Check if database was created
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
"""

# Create users table which will have the usernames and passwords saved
cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INT AUTO_INCREMENT PRIMARY KEY,\
                                                  username VARCHAR(20),\
                                                  password VARCHAR(20))")

"""
# Check if table was created
cursor.execute("SELECT * FROM users")
for column in cursor.description:
    print(column)
"""

"""
# Insert into table users admin record to control who register
sql_command = "INSERT INTO users (username,password) VALUES (%s,%s)"
values = ("JassemShe","JissShe")
cursor.execute(sql_command,values)
mydb.commit()
"""

"""
# Show records in users table
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
for record in result:
    print(record)
"""


def login_valid():
    """This funtion is responible to check if username and password are correct and if correct
    will call login_fun to enter the option menu"""

    username_try = username_box.get()
    password_try = password_box.get()

    # Get users in data
    cursor.execute("SELECT username FROM users")
    users_result = cursor.fetchall()
    user_records = [record[0] for record in users_result]

    # Check if username is in data
    if username_try in user_records:
        # Check if the password match
        sql_command = "SELECT password FROM users WHERE username IN (%s)"
        value = (username_try,)
        cursor.execute(sql_command,value)
        password_result = cursor.fetchall()
        password_records = [record[0] for record in password_result]
        if password_try in password_records:
            root.destroy()
            login_fun()
        else:
            messagebox.showerror(title="Warning",message="Wrong Password")
    else:
        messagebox.showerror(title="Warning",message="Wrong Username")


# Cafe name title label
cafe_name_label = Label(root,text="Cafe Managment System",font=("Arial",16)).grid(row = 0 , column = 0,columnspan=2,sticky=W)

# Create username and password labels
username_label = Label(root,text="Username",font=("Arial",12)).grid(row = 1, column = 0,pady=(50,0),padx=(40,0))
password_label = Label(root,text="Password",font=("Arial",12)).grid(row = 2, column = 0,pady=(20,0),padx=(40,0))

# Create entry boxes for username and passwosrd
username_box = Entry(root)
username_box.grid(row = 1,column =1,pady=(60,0),padx=(5,0))
password_box = Entry(root)
password_box.grid(row = 2,column =1,pady=(20,0),padx=(5,0))

# Create login button
login_button = Button(root,text="Login",font=("Arial",12),command=login_valid)
login_button.grid(row = 3,column =1,pady=(20,0),padx=(5,0))

# Create register button
register_button = Button(root,text="Register",command=register_fun)
register_button.grid(row = 4,column =1,pady=(20,0),padx=(5,0))


root.mainloop()
