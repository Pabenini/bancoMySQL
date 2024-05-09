import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Imobiliaria"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Pessoa (idPessoa INT NOT NULL AUTO_INCREMENT, nome VARCHAR(45) NOT NULL, email VARCHAR(100) NOT NULL, endereco VARCHAR(100) NOT NULL, dataNascimento DATE NOT NULL, sexo VARCHAR(10) NOT NULL, cpf INT NOT NULL, PRIMARY KEY (idPessoa))")
mycursor.execute("CREATE TABLE Telefone (idTelefone INT NOT NULL AUTO_INCREMENT, numero INT NOT NULL, ddd INT NOT NULL, operadora VARCHAR(45) NOT NULL, fk_Pessoa INT NOT NULL, PRIMARY KEY (idTelefone), FOREIGN KEY (fk_Pessoa) REFERENCES Pessoa (idPessoa))")
mycursor.execute("CREATE TABLE EncontrarImovel (idEncontrarImovel INT NOT NULL AUTO_INCREMENT, endereco VARCHAR(100) NOT NULL, data DATE NOT NULL, servico VARCHAR(45) NOT NULL, PRIMARY KEY (idEncontrarImovel))")
mycursor.execute("CREATE TABLE AlugarVender (idAlugarVender INT NOT NULL AUTO_INCREMENT, endereco VARCHAR(100) NOT NULL, valor FLOAT NOT NULL, alugar VARCHAR(45) NOT NULL, imagem BLOB NOT NULL, comprar VARCHAR(45) NOT NULL, fk_Telefone INT NOT NULL, fk_EncontrarImovel INT NOT NULL, fk_Pessoa INT NOT NULL, PRIMARY KEY (idAlugarVender), FOREIGN KEY (fk_Pessoa) REFERENCES Pessoa (idPessoa), FOREIGN KEY (fk_EncontrarImovel) REFERENCES EncontrarImovel (idEncontrarImovel), FOREIGN KEY (fk_Telefone) REFERENCES Telefone (idTelefone))")