import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1111",
  db="menagerie"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner")
for row in mycursor.fetchall():
    print(row)

mycursor.close()
mydb.close()

