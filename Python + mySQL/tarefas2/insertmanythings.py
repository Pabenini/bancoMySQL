import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Tarefas2"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tarefa (nome, data, descricao, status) VALUES (%s, %s, %s, %s)"
val = [
  ("tarefa", "2024-04-30", "Fazer uma database chamada tarefas", "terminada"),
  ("Lucy", "2024-01-26", "Planejar viajem", "terminada"),
  ("Fernanda", "2024-03-23", "Fazer um site", "pendente"),
  ("Carlos", "2024-12-11", "Comprar Plantas", "Não terminada"),
  ("Bruno", "2024-09-05", "Fabricar bolsas", "Não terminada"),
  ("Paulo", "2024-07-05", "Limpar a casa", "Não terminada"),
  ("Rafaella", "2024-04-06", "Terminar o curso", "terminada"),
  ("Maria", "2024-11-08", "Fazer tarefa", "Não terminada"),
  ("Julia", "2024-08-21", "Incomendar bolo", "Não terminada"),
  ("Carla", "2024-10-10", "Jogar bola", "Não terminada"),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")