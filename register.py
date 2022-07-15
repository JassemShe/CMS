from tkinter import *
from tkinter import messagebox
import mysql.connector


# Create a mysql instant and connect it (will add database later when create it)
mydb = mysql.connector.connect(
                  host = "127.0.0.1",
                  user = "root",
                  passwd = "jmjmaaskull",
                  database = "cms")

# Create cursor object
cursor = mydb.cursor()


def register_fun():
    """This function will open a new window where user will give details to check if he is admin
    then if true he will be able to register new username to the system"""
    register = Tk()
    register.title("Register")
    register.geometry("340x380")


    def add():
        """This function is responsible for checking if the admin and passowrd and current
        are currect and then add new user to the database"""

        # Get values from boxes
        admin = admin_box.get()
        admin_password = admin_password_box.get()

        # Check if admin is valid (New admins can be added later)
        if admin in ('JassemShe') and admin_password in ('JissShe') and admin != '' and admin_password != '':

            # Add new user
            newuser = new_user_box.get()
            newuser_password = new_user_password_box.get()

            # Check if the newuser is not already exits
            cursor.execute("SELECT username FROM users")
            result = cursor.fetchall()
            records = [record[0] for record in result]
            if newuser not in records:
                sql_command = "INSERT INTO users (username,password) VALUES (%s,%s)"
                values = (newuser,newuser_password)
                cursor.execute(sql_command,values)
                mydb.commit()

                # Confirm add
                messagebox.showinfo(title="Done",message="New user Added")

                # Clear boxes
                admin_box.delete(0,END)
                admin_password_box.delete(0,END)
                new_user_box.delete(0,END)
                new_user_password_box.delete(0,END)
            else:
             messagebox.showerror(title="Warning",message="Username already exits")
        else:
            messagebox.showerror(title="Warning",message="Wrong Admin name or password")




    # Cafe name title label
    register_label = Label(register,text="Register",font=("Arial",16)).grid(row = 0 , column = 0,columnspan=2,sticky=W)

    # Create admin and password labels
    admin_label = Label(register,text="Admin",font=("Arial",12)).grid(row = 1, column = 0,pady=(50,0),padx=(40,0))
    admin_password_label = Label(register,text="Password",font=("Arial",12)).grid(row = 2, column = 0,pady=(20,0),padx=(40,0))

    # Create entry boxes for username and passwosrd
    admin_box = Entry(register)
    admin_box.grid(row = 1,column =1,pady=(60,0),padx=(5,0))
    admin_password_box = Entry(register)
    admin_password_box.grid(row = 2,column =1,pady=(20,0),padx=(5,0))

    # Add new user label
    new_user_label = Label(register,text="Add New User",font=("Arial",13)).grid(row = 3 , column = 0 ,columnspan=2,sticky=W,pady=(30,0))

    # Create new user and password labels
    new_user_label = Label(register,text="New user",font=("Arial",12)).grid(row = 4, column = 0,pady=(20,0),padx=(40,0))
    new_user_password_label = Label(register,text="Password",font=("Arial",12)).grid(row = 5, column = 0,pady=(10,0),padx=(40,0))

    # Create entry boxes for new users and passwosrd
    new_user_box = Entry(register)
    new_user_box.grid(row = 4,column =1,pady=(20,0),padx=(5,0))
    new_user_password_box = Entry(register)
    new_user_password_box.grid(row = 5,column =1,pady=(10,0),padx=(5,0))

    # Create add button
    add_button = Button(register,text="Add",font=("Arial",12),command=add)
    add_button.grid(row = 6,column =1,pady=(20,0),padx=(5,0))




