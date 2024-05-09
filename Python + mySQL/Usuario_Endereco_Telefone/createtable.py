import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Usuario_Endereco_Telefone"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Endereco (idEndereco INT NOT NULL AUTO_INCREMENT, logradouro VARCHAR(50) NOT NULL, bairro VARCHAR(50) NOT NULL, cep INT NOT NULL, cidade VARCHAR(50) NOT NULL, estado VARCHAR(50) NOT NULL, complemento VARCHAR(50) NOT NULL, PRIMARY KEY (idEndereco))")
mycursor.execute("CREATE TABLE Pessoa (idPessoa INT NOT NULL AUTO_INCREMENT, cpf INT NOT NULL, nome VARCHAR(50) NOT NULL, data_nascimento DATE NOT NULL, sexo VARCHAR(10) NOT NULL, numero_casa INT NOT NULL, fk_Endereco INT NOT NULL, PRIMARY KEY (idPessoa), FOREIGN KEY (fk_Endereco) REFERENCES Endereco (idEndereco))")
mycursor.execute("CREATE TABLE Telefone (idTelefone INT NOT NULL AUTO_INCREMENT, numero INT NOT NULL, ddd INT NOT NULL, operadora VARCHAR(45) NOT NULL, fk_Pessoa INT NOT NULL, PRIMARY KEY (idTelefone), FOREIGN KEY (fk_Pessoa) REFERENCES Pessoa (idPessoa))")