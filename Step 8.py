import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1111"
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS managerie")


mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


mydb.close()