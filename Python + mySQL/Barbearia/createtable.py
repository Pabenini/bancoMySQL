# isso é essencial ter em todos os codigos
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Barbearia"
)

mycursor = mydb.cursor()

# cria a tabela clientes
mycursor.execute("CREATE TABLE Cliente (idCliente INT NOT NULL AUTO_INCREMENT, nome VARCHAR(45) NOT NULL, dataNascimento DATE NOT NULL, whatsapp DECIMAL(9) NOT NULL, PRIMARY KEY(idCliente))")

# cria a tabela servico
mycursor.execute("CREATE TABLE Servico (idServico INT NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, valor FLOAT NOT NULL, descricao VARCHAR(100), PRIMARY KEY(idServico))")

# cria a tabela agenda
mycursor.execute("CREATE TABLE Agenda (idAgenda INT NOT NULL AUTO_INCREMENT, data DATETIME NOT NULL, dia DATE NOT NULL, hora TIME NOT NULL, pago CHAR(1) NOT NULL, fk_idCliente INT NOT NULL, fk_idServico INT NOT NULL, PRIMARY KEY (idAgenda), FOREIGN KEY (fk_idCliente) REFERENCES Cliente (idCliente), FOREIGN KEY (fk_idServico) REFERENCES Servico (idServico))")
