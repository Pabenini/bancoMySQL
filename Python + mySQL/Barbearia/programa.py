# esse codigo é para criar uma conexão com o xampp
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)