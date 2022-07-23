from tkinter import *
from tkinter import messagebox
import mysql.connector


def main_gui():
    """This the main window of the program."""
    import register

    root = Tk()
    root.title("Cafe System Managment")
    root.geometry("320x280")

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
        global username_try

        login = Tk()
        login.title("Option menu")
        login.geometry("320x340")

        def log_out():
            """This funtion will close login window and open mainGUI window"""
            login.destroy()
            main_gui()

        # Create user name label to show which user is using the program currenty
        user_name_label = Label(login,text =username_try)
        user_name_label.grid(column =  0 ,row = 0,padx=5,pady=5)

        # Create Sales operations button
        sales_button = Button(login, text = " Sales operations ",font=("Arial",16))
        sales_button.grid(column = 1, row =1,pady=(60,10))

        # Create Store button
        store_button = Button(login, text = "Store",font=("Arial",16),width=15)
        store_button.grid(column = 1, row = 2,pady=(10,20))

        # Create log out button
        logout_button = Button(login, text = "Log out",font=("Arial",16),width=15,command=log_out)
        logout_button.grid(column = 1, row = 3)



    def login_valid():
        """This funtion is responible to check if username and password are correct and if correct
        will call login_fun to enter the option menu"""
        global username_try

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
    password_box = Entry(root,show="*")
    password_box.grid(row = 2,column =1,pady=(20,0),padx=(5,0))

    # Create login button
    login_button = Button(root,text="Login",font=("Arial",12),command=login_valid)
    login_button.grid(row = 3,column =1,pady=(20,0),padx=(5,0))

    # Create register button
    register_button = Button(root,text="Register",command=register.register_fun)
    register_button.grid(row = 4,column =1,pady=(20,0),padx=(5,0))

    root.mainloop()

main_gui()
