import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1111",
  db="menagerie"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT name, birth, MONTH(birth) FROM pet")
for row in mycursor.fetchall():
    print(row)

mycursor.close()
mydb.close()
