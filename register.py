from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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
    register.geometry("320x380")


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


    def deploy():
        """This function is resplosilbe for checking admin name and password are correct and open
        a new window to deploy system to the cafe current status."""

        def reset():
           response = messagebox.askquestion(title = "Reset" ,message="Delete and reset all records?")
           if response == 1:
            pass


        # Get values from boxes
        admin = admin_box.get()
        admin_password = admin_password_box.get()

        # Check if admin is valid (New admins can be added later)
        if admin in ('JassemShe') and admin_password in ('JissShe') and admin != '' and admin_password != '':
            deploy = Tk()
            deploy.title("Fresh Start")
            deploy.geometry("360x375")

            """item price"""
            # Create item price label and drop box for item prices under it
            item_price_label = Label(deploy,text = "Item price",font=("Arial",12)).grid(row = 0 , column = 0 ,pady = (10,0),padx = (0,5),sticky=W)

            items_list = ["0.05","0.10","0.15","0.20","0.25","0.30","0.35","0.40","0.45","0.50","0.55","0.60","0.65","0.70","0.75","0.80","0.85",\
                          "0.90","0.95","1.00"]
            item_drop = ttk.Combobox(deploy,values = items_list,state="readonly")
            item_drop.current(0)
            item_drop.grid(row = 1, column = 0 , pady = (0,0))

            # Create item quantity label and quanity box under it
            item_quantity_label = Label(deploy,text = "Q",font=("Arial",12)).grid(row = 0 ,column = 1 ,pady = (15,0) ,padx=(10 , 5))

            item_quantity_box = Entry(deploy,width = 10)
            item_quantity_box.grid(row = 1, column = 1 , pady = (0,0), padx =(10,5))

            # Create add item button
            add_item_button = Button(deploy,text = "Add items",font=("Arial",10))
            add_item_button.grid(row = 1 , column = 2 , pady = (0,0), padx = (10 ,5))

            """tea cup"""
            # Create tea cup label and drop box for prices under it
            tea_cup_label = Label(deploy,text = "Tea cup price",font=("Arial",12)).grid(row = 2 , column = 0 ,pady = (20,0),padx = (0,5),sticky=W)

            tea_list = ["0.25","0.30","0.35","0.40","0.45","0.50"]
            tea_drop = ttk.Combobox(deploy,values = tea_list,state="readonly")
            tea_drop.current(2)
            tea_drop.grid(row = 3, column = 0 , pady = (0,0))

            # Create cup quantity label and quanity box under it
            tea_quantity_label = Label(deploy,text = "Q",font=("Arial",12)).grid(row = 2 ,column = 1 ,pady = (15,0) ,padx=(10 , 5))

            tea_quantity_box = Entry(deploy,width = 10)
            tea_quantity_box.grid(row = 3, column = 1 , pady = (0,0), padx =(10,5))

            # Create add tea button
            add_tea_button = Button(deploy,text = "Add tea cups",font=("Arial",10))
            add_tea_button.grid(row = 3 , column = 2 , pady = (0,0), padx = (10 ,5))

            """coffe cup"""
            # Create  cup label and drop box for prices under it
            coffe_cup_label = Label(deploy,text = "Coffe cup price",font=("Arial",12)).grid(row = 4 , column = 0 ,pady = (20,0),padx = (0,5),sticky=W)

            coffe_list = ["0.35","0.40","0.45","0.50","0.55","0.60","0.65","0.70","0.80","0.85","0.90","0.95","1.00"]
            coffe_drop = ttk.Combobox(deploy,values = coffe_list,state="readonly")
            coffe_drop.current(3)
            coffe_drop.grid(row = 5, column = 0 , pady = (0,0))

            # Create cup quantity label and quanity box under it
            coffe_quantity_label = Label(deploy,text = "Q",font=("Arial",12)).grid(row = 4 ,column = 1 ,pady = (15,0) ,padx=(10 , 5))

            coffe_quantity_box = Entry(deploy,width = 10)
            coffe_quantity_box.grid(row = 5, column = 1 , pady = (0,0), padx =(10,5))

            # Create add tea button
            add_coffe_button = Button(deploy,text = "Add coffe cups",font=("Arial",10))
            add_coffe_button.grid(row = 5 , column = 2 , pady = (0,0), padx = (10 ,5))

            """Cash"""
            # Create cash label
            cash_label = Label(deploy,text = "Cash",font=("Arial",12)).grid(row = 6 , column = 0 ,pady = (50,0),padx = (0,0))

            cash_box = Entry(deploy,width = 10)
            cash_box.grid(row = 6, column = 1 , pady = (50,0),padx=(0,0))

            add_cash_button = Button(deploy,text = "Add cash",font=("Arial",10))
            add_cash_button.grid(row = 6 , column = 2,padx = (0,0),pady=(50,0))

            # Create reset button
            reset_button = Button(deploy, text = "Reset all",font = ("Arial",12),command = reset)
            reset_button.grid(row = 7 , column = 0, pady = (50,0),sticky = W+S)




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
    add_button = Button(register,text="Add new user",font=("Arial",12),command=add)
    add_button.grid(row = 6,column =1,pady=(20,0),padx=(5,0))

    # Create fresh start button
    fresh_start_button = Button(register,text="Deploy system",font=("Arial",12),relief=RIDGE,command=deploy)
    fresh_start_button.grid(row = 7,column =1,pady=(5,0),padx=(5,0))



