import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", 
  database="iwavjezba4"
)

if mydb.is_connected():
    print("Connected to MySQL database")

mydb.close()
