import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1111",
  db="menagerie"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pet")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mydb.commit()
mydb.close()
