import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111"
)

print(mydb)

