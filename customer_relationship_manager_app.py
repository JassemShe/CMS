from tkinter import *
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title("Customer relationship manager")
root.geometry("400x600")


# Create clear boxes function
def clear():
    first_name_box.delete(0,END)
    last_name_box.delete(0,END)
    zipcode_box.delete(0,END)
    price_paid_box.delete(0,END)
    email_box.delete(0,END)
    address_1_box.delete(0,END)
    address_2_box.delete(0,END)
    city_box.delete(0,END)
    state_box.delete(0,END)
    country_box.delete(0,END)
    phone_box.delete(0,END)
    payment_method_box.delete(0,END)
    discount_code_box.delete(0,END)


# Create isnert add customer to table funtion
def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, adress_1, adress_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" # %s is a place holder
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address_1_box.get(), address_2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    cursor.execute(sql_command,values)

    # Commit changes
    mydb.commit()

    # Call clear funtion and clear all boxes
    clear()


# Create function to show customer record when lookup by last name
def lookup():
   # Show record in new window
   lookup_window = Tk()
   lookup_window.title("Look up customer")
   lookup_window.geometry("1200x600")


   # Get the value of drop box
   selected = drop.get()

   # Query to get customer record by what selected in drop box
   if selected == "Search by...":
     return

   if selected == "Last name":
      customer_last_name = lookup_box.get().lower()
      sql_command = "SELECT * FROM customers WHERE LOWER(last_name) = %s"
      name = (customer_last_name, )
      cursor.execute(sql_command, name)
      result = cursor.fetchall()
      if not result:
          show_records_label = Label(lookup_window,text = "No record found...").grid(row = 0 , column = 0,sticky = W, padx = 10)
      else:
         for index,record in enumerate(result):
           num = 0
           edit_button = Button(lookup_window, text = "Edit")
           edit_button.grid(row = index , column = 0, padx = 10)
           for variable in record:
              show_records_label = Label(lookup_window,text = variable).grid(row = index , column = num + 1,sticky = W, padx = 10)
              num += 1

   if selected == "Email":
      customer_email = lookup_box.get().lower()
      sql_command = "SELECT * FROM customers WHERE LOWER(email) = %s"
      email = (customer_email, )
      cursor.execute(sql_command, email)
      result = cursor.fetchall()
      if not result:
          show_records_label = Label(lookup_window,text = "No record found...").grid(row = 0 , column = 0,sticky = W, padx = 10)
      else:
         for index,record in enumerate(result):
           num = 0
           edit_button = Button(lookup_window, text = "Edit")
           edit_button.grid(row = index , column = 0, padx = 10)
           for variable in record:
              show_records_label = Label(lookup_window,text = variable).grid(row = index , column = num+1,sticky = W, padx = 10)
              num += 1

   if selected == "Customer id":
      customer_last_name = lookup_box.get().lower()
      sql_command = "SELECT * FROM customers WHERE user_id = %s"
      name = (customer_last_name, )
      cursor.execute(sql_command, name)
      result = cursor.fetchall()
      if not result:
          show_records_label = Label(lookup_window,text = "No record found...").grid(row = 0 , column = 0,sticky = W, padx = 10)
      else:
         for index,record in enumerate(result):
           num = 0
           edit_button = Button(lookup_window, text = "Edit")
           edit_button.grid(row = index , column = 0, padx = 10)
           for variable in record:
              show_records_label = Label(lookup_window,text = variable).grid(row = index , column = num+1,sticky = W, padx = 10)
              num += 1


   """
   # Query to get customer record
   customer_last_name = lookup_box.get().lower()
   sql_command = "SELECT * FROM customers WHERE LOWER(last_name) = %s"
   name = (customer_last_name, )
   cursor.execute(sql_command, name)
   result = cursor.fetchall()
   if not result:
      show_records_label = Label(lookup_window,text = "No record found...").grid(row = 0 , column = 0,sticky = W, padx = 10)
   else:
     for index,record in enumerate(result):
        num = 0
        for variable in record:
           show_records_label = Label(lookup_window,text = variable).grid(row = index , column = num,sticky = W, padx = 10)
           num += 1
    """

# Create funtion to show the records in the table
def list_customers():
       # Show records in new window
       list_customers_window = Tk()
       list_customers_window.title("Customers Records")
       list_customers_window.geometry("1200x600")


       # Function to export that into csv file
       def export(result):
          with open("Customers.csv","w",newline='') as f:
            writer = csv.writer(f,dialect = 'excel')
            for row in result:
              writer.writerow(row)


       # Create records headers
       first_name_label = Label(list_customers_window, text = "First Name", font=("Helvetica",12)).grid(row = 0, column = 0, sticky=W, padx = 10,pady = 10)
       last_name_label = Label(list_customers_window, text = "Last Name", font=("Helvetica",12)).grid(row = 0, column = 1, sticky=W, padx = 10,pady = 10)
       zipcode_label = Label(list_customers_window, text = "Zipcode", font=("Helvetica",12)).grid(row = 0, column = 2, sticky=W, padx = 10,pady = 10)
       price_paid_label = Label(list_customers_window, text = "Price Paid", font=("Helvetica",12)).grid(row = 0, column = 3, sticky=W, padx = 10,pady = 10)
       user_id_label = Label(list_customers_window, text = "User id", font=("Helvetica",12)).grid(row = 0, column = 4, sticky=W, padx = 10,pady = 10)
       email_label = Label(list_customers_window, text = "Email", font=("Helvetica",12)).grid(row = 0, column = 5, sticky=W, padx = 10,pady = 10)
       address_1_label = Label(list_customers_window, text = "Address 1", font=("Helvetica",12)).grid(row = 0, column = 6, sticky=W, padx = 10,pady = 10)
       address_2_label = Label(list_customers_window, text = "Address 2", font=("Helvetica",12)).grid(row = 0, column = 7, sticky=W, padx = 10,pady = 10)
       city_label = Label(list_customers_window, text = "City", font=("Helvetica",12)).grid(row = 0, column = 8, sticky=W, padx = 10,pady = 10)
       state_label = Label(list_customers_window, text = "State", font=("Helvetica",12)).grid(row = 0, column = 9, sticky=W, padx = 10,pady = 10)
       country_label = Label(list_customers_window, text = "Country", font=("Helvetica",12)).grid(row = 0, column = 10, sticky=W, padx = 10,pady = 10)
       phone_label = Label(list_customers_window, text = "Phone", font=("Helvetica",12)).grid(row = 0, column = 11, sticky=W, padx = 10,pady = 10)
       payment_method_label = Label(list_customers_window, text = "Payment Method", font=("Helvetica",12)).grid(row = 0, column = 12, sticky=W, padx = 10,pady = 10)
       discount_code_label = Label(list_customers_window, text = "Discount Code", font=("Helvetica",12)).grid(row = 0, column = 13, sticky=W, padx = 10,pady = 10)

       # Make query to get records in table
       cursor.execute("SELECT * FROM customers")
       result = cursor.fetchall()
       for index,record in enumerate(result):
           num = 0
           for variable in record:
            show_records_label = Label(list_customers_window,text = variable).grid(row = index + 1 , column = num,sticky = W, padx = 10)
            num += 1

       # Create a button to export data to csv
       csv_button = Button(list_customers_window,text = "Export as CSV", command = lambda: export(result))
       csv_button.grid(row = index + 2 , column = 0 )


#Create a sql intsant and connect to it
mydb  = mysql.connector.connect(
             host = "localhost",
             user = "root",
             passwd = "jmjmaaskull",
             database = "codemy") # We add the database if we already have one or after we have created one


#print(mydb) # Check if the connection was created


# Create cursor object
cursor = mydb.cursor()

"""
# Create databases
cursor.execute("CREATE DATABASE codemy")
"""

"""
# Check if database was created
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
"""

"""
# Create a table
cursor.execute("CREATE TABLE customers (first_name VARCHAR(50), last_name VARCHAR(50), zipcode INT(10), price_paid DECIMAL(10,2), user_id INT AUTO_INCREMENT PRIMARY KEY)")
"""

"""
# Show table columns
cursor.execute("SELECT * FROM customers")
for obj in cursor.description:
    print(obj)
"""

# Better way to create the table columns in diffrent lines and check if the table already exits
cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(50), \
                                                      last_name VARCHAR(50), \
                                                      zipcode INT(10), \
                                                      price_paid DECIMAL(10,2), \
                                                      user_id INT AUTO_INCREMENT PRIMARY KEY)")

"""
# Alter table and add columns
cursor.execute("ALTER TABLE customers ADD (email VARCHAR(50), \
                                           adress_1 VARCHAR(50), \
                                           adress_2 VARCHAR(50), \
                                           city VARCHAR(50), \
                                           state VARCHAR(50), \
                                           country VARCHAR(50), \
                                           phone VARCHAR(50), \
                                           payment_method VARCHAR(50), \
                                           discount_code VARCHAR(50))")
"""

"""
# Show changes
cursor.execute("SELECT * FROM customers")
for obj in cursor.description:
    print(obj)
"""

# Create title label in the GUI
title_label = Label(root,text="Codemy Customers Database",font=("Helvetica",16)).grid(row=0,column=0,columnspan=2,pady=10)

# Create label for each column in table
first_name_label = Label(root, text = "First Name").grid(row = 1, column = 0, sticky=W, padx = 10)
last_name_label = Label(root, text = "Last Name").grid(row = 2, column = 0, sticky=W, padx = 10)
zipcode_label = Label(root, text = "Zipcode").grid(row = 3, column = 0, sticky=W, padx = 10)
price_paid_label = Label(root, text = "Price Paid").grid(row = 4, column = 0, sticky=W, padx = 10)
email_label = Label(root, text = "Email").grid(row = 5, column = 0, sticky=W, padx = 10)
address_1_label = Label(root, text = "Address 1").grid(row = 6, column = 0, sticky=W, padx = 10)
address_2_label = Label(root, text = "Address 2").grid(row = 7, column = 0, sticky=W, padx = 10)
city_label = Label(root, text = "City").grid(row = 8, column = 0, sticky=W, padx = 10)
state_label = Label(root, text = "State").grid(row = 9, column = 0, sticky=W, padx = 10)
country_label = Label(root, text = "Country").grid(row = 10, column = 0, sticky=W, padx = 10)
phone_label = Label(root, text = "Phone").grid(row = 11, column = 0, sticky=W, padx = 10)
payment_method_label = Label(root, text = "Payment Method").grid(row = 12, column = 0, sticky=W, padx = 10)
discount_code_label = Label(root, text = "Discount Code").grid(row = 13, column = 0, sticky=W, padx = 10)

# Create entry boxes for each column in table (here cant grid for entry in same line bcause some funtions wont work later like delete)
first_name_box = Entry(root)
first_name_box.grid(row = 1, column = 1, pady = 5)

last_name_box = Entry(root)
last_name_box.grid(row = 2, column = 1, pady = 5)

zipcode_box = Entry(root)
zipcode_box.grid(row = 3, column = 1, pady = 5)

price_paid_box = Entry(root)
price_paid_box.grid(row = 4, column = 1, pady = 5)

email_box = Entry(root)
email_box.grid(row = 5, column = 1, pady = 5)

address_1_box = Entry(root)
address_1_box.grid(row = 6, column = 1, pady = 5)

address_2_box = Entry(root)
address_2_box.grid(row = 7, column = 1, pady = 5)

city_box = Entry(root)
city_box.grid(row = 8, column = 1, pady = 5)

state_box = Entry(root)
state_box.grid(row = 9, column = 1, pady = 5)

country_box = Entry(root)
country_box.grid(row = 10, column = 1, pady = 5)

phone_box = Entry(root)
phone_box.grid(row = 11, column = 1, pady = 5)

payment_method_box = Entry(root)
payment_method_box.grid(row = 12, column = 1, pady = 5)

discount_code_box = Entry(root)
discount_code_box.grid(row = 13, column = 1, pady = 5)


# Create drop down box to search data by specific column
drop = ttk.Combobox(root,values = ["Search by...","Last name","Email","Customer id"],state="readonly")
drop.current(0)
drop.grid(row = 15, column = 0 , sticky = W , padx = 10,pady = (15,0))


# Create entry box for lookup
lookup_box = Entry(root)
lookup_box.grid(row = 15, column = 1, pady = (15,0))


# Create button to insert(add) cutoemr into table
add_customer_button = Button(root,text = "Add Customer To Database", command = add_customer)
add_customer_button.grid(row = 14, column = 0, padx = 10, sticky = W)

# Create button to clear boxes
clear_fields_button = Button(root, text = "Clear fields",command = clear)
clear_fields_button.grid(row = 14, column = 1) # No need to give it and pads because it will be same as the column it its line

# Create a button to lookup customer by last name
lookup_button = Button(root,text="Search",command = lookup)
lookup_button.grid(row = 16, column = 1,padx = 10 , pady=(0,15),columnspan=3)

# Create button to show customers in the data (records in the data)
list_customers_button = Button(root,text="List all customers", command = list_customers)
list_customers_button.grid(row = 17, column = 0, padx = 10, sticky = W)






root.mainloop()
