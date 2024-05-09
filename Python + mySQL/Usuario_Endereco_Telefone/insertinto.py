import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Usuario_Endereco_Telefone"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tarefa (nome, data, descricao, status) VALUES (%s, %s, %s, %s)"
val = ("Pedro", "2024-05-25", "Vestibular", "Em andamento")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")