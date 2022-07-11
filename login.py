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


def login_fun():
    """This function will open a new window if the username and password are valid.

    The window will inculde the options the user can use in the application"""


    login = Tk()
    login.title("Option menu")
    login.geometry("300x400")


    # Create Sales operations button
    sales_button = Button(login, text = " Sales operations ",font=("Arial",16))
    sales_button.grid(column = 0, row = 0,padx=70,pady=(100,10))


    # Create Store button
    store_button = Button(login, text = "Store",font=("Arial",16),width=15)
    store_button.grid(column = 0, row = 1,padx=70,pady=(10,20))

    # Create log out button
    store_button = Button(login, text = "Log out",font=("Arial",16),width=15)
    store_button.grid(column = 0, row = 2,padx=70)



    login.mainloop()

