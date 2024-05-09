import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Tarefas2"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE tarefa ADD COLUMN idTarefas INT AUTO_INCREMENT PRIMARY KEY")