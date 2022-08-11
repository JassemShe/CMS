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


# Create a mysql instant and connect it (will add database later when create it)
mydb = mysql.connector.connect(
                  host = "127.0.0.1",
                  user = "root",
                  passwd = "jmjmaaskull",
                  database = "cms")

# Create cursor object
cursor = mydb.cursor()





# Create items table
cursor.execute("CREATE TABLE IF NOT EXISTS items (item_id INT AUTO_INCREMENT PRIMARY KEY,\
                                                      0_05 INTEGER,\
                                                      0_10 INTEGER,\
                                                      0_15 INTEGER,\
                                                      0_20 INTEGER,\
                                                      0_25 INTEGER,\
                                                      0_30 INTEGER,\
                                                      0_35 INTEGER,\
                                                      0_40 INTEGER,\
                                                      0_45 INTEGER,\
                                                      0_50 INTEGER,\
                                                      0_55 INTEGER,\
                                                      0_60 INTEGER,\
                                                      0_65 INTEGER,\
                                                      0_70 INTEGER,\
                                                      0_75 INTEGER,\
                                                      0_80 INTEGER,\
                                                      0_85 INTEGER,\
                                                      0_90 INTEGER,\
                                                      1_00 INTEGER)")

# Create items table
cursor.execute("CREATE TABLE IF NOT EXISTS tea_cup (tea_id INT AUTO_INCREMENT PRIMARY KEY,\
                                                      0_25 INTEGER,\
                                                      0_30 INTEGER,\
                                                      0_35 INTEGER,\
                                                      0_40 INTEGER,\
                                                      0_45 INTEGER,\
                                                      0_50 INTEGER)")

# Create items table
cursor.execute("CREATE TABLE IF NOT EXISTS coffe_cup (coffe_id INT AUTO_INCREMENT PRIMARY KEY,\
                                                      0_35 INTEGER,\
                                                      0_40 INTEGER,\
                                                      0_45 INTEGER,\
                                                      0_50 INTEGER,\
                                                      0_55 INTEGER,\
                                                      0_60 INTEGER,\
                                                      0_65 INTEGER,\
                                                      0_70 INTEGER,\
                                                      0_75 INTEGER,\
                                                      0_80 INTEGER,\
                                                      0_85 INTEGER,\
                                                      0_90 INTEGER,\
                                                      1_00 INTEGER)")

# Create items table
cursor.execute("CREATE TABLE IF NOT EXISTS cash (cash_id INT AUTO_INCREMENT PRIMARY KEY,current_cash DECIMAL(6,2))")

"""
# Check if table was created
cursor.execute("SELECT * FROM items,tea_cup,coffe_cup,cash")
for column in cursor.description:
    print(column)
"""
