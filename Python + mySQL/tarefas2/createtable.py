import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Tarefas2"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE tarefas (idTarefas INT NOT NULL AUTO_INCREMENT, nome VARCHAR(45) NOT NULL, data DATE NOT NULL, descricao VARCHAR(200) NOT NULL, status VARCHAR(15) NOT NULL, PRIMARY KEY(idTarefas))")