# isso é essencial ter em todos os codigos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

# mostra todas as databases existentes
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)