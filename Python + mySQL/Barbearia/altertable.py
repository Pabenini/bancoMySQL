# isso é essencial ter em todos os codigos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Barbearia"
)

mycursor = mydb.cursor()

# adiciona novas colunas a tabelas ja criadas
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")