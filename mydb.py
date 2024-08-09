# So we have created a database with teh name "spanbase" and we create a database here

import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "12345678",
)

# Now we do prepare a cursor object using the cursor() method of the mysql

cursor_object = database.cursor()

# Now we create a database using the execute() method of the cursor object

cursor_object.execute("CREATE DATABASE spanbase")

print('The database is created successfully')