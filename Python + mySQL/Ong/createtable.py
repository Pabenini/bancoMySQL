import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Ong"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Usuario (idUsuario INT NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL, endereco VARCHAR(50) NOT NULL, whatsapp INT NOT NULL, PRIMARY KEY(idUsuario))")
mycursor.execute("CREATE TABLE Ong (idOng INT NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL, endereco VARCHAR(50) NOT NULL, whatsapp INT NOT NULL, PRIMARY KEY(idOng))")
mycursor.execute("CREATE TABLE Ocorrencia (idOcorrencia INT NOT NULL AUTO_INCREMENT, descricao VARCHAR(100) NOT NULL, data DATE NOT NULL, imagem BLOB NOT NULL, fk_idUsuario INT NOT NULL, fk_idOng INT NOT NULL, PRIMARY KEY (idOcorrencia), FOREIGN KEY (fk_idUsuario) REFERENCES Usuario (idUsuario), FOREIGN KEY (fk_idOng) REFERENCES Ong (idOng))")