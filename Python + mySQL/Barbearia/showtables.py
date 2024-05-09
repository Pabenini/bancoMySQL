# isso é essencial ter em todos os codigos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Barbearia"
)

mycursor = mydb.cursor()

# mostrar todas as tabelas existentes
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)