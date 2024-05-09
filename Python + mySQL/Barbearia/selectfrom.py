# isso é essencial ter em todos os codigos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Barbearia"
)

mycursor = mydb.cursor()

# mostra todo adicionado/colocado na tabela
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)