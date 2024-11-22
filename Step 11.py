import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1111",
  db="menagerie"
)

mycursor = mydb.cursor()
mycursor.execute("DESCRIBE pet")
for row in mycursor:
    print(row)
