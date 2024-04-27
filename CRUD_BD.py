import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost', 
    user = 'usuario',
    password = 'senha',
    database = 'banco de dados', 
)

cursor = conexao.cursor()

# ************************ CRIANDO A TABELA  ***************************
comando = '''
CREATE TABLE jogador (
    idJogador INT PRIMARY KEY AUTO_INCREMENT,
    nomeJogador VARCHAR(100) NOT NULL,
    posicao ENUM('Zagueiro', 'Meia', 'Atacante') NOT NULL,
    nivel INT NULL
)
'''
cursor.execute(comando)
conexao.commit()

# *********************** VISUALIZAR TABELA ATUAL *********************
comando2 = 'SELECT * FROM jogador;'
cursor.execute(comando2)
resultado = cursor.fetchall() #ler
for i in resultado:
    print(i)
print("*"*30)

# ********************** INSERT JOGADOR ******************************
nomeJogador = 'Joao'
posicao = "Atacante"
nivel = 8
comando = f'INSERT INTO jogador(nomeJogador, posicao, nivel) VALUES ("{nomeJogador}", "{posicao}", "{nivel}")'
cursor.execute(comando)
conexao.commit() # editar

# ********************** DELETE JOGADOR *******************************
nomeJogador = "Dato"
comando = f'DELETE FROM jogador WHERE nomeJogador = "{nomeJogador}"'
cursor.execute(comando)
conexao.commit()

# *********************** UPDATE JOGADOR ***********************************
nomeJogador = "Tiago"
nivel = 10
comando = f'UPDATE jogador SET nivel = "{nivel}" WHERE nomeJogador = "{nomeJogador}"'
cursor.execute(comando)
conexao.commit()

# *********************** VISUALIZAR TABELA ATUAL *********************
comando3 = 'SELECT * FROM jogador;'
cursor.execute(comando3)
resultado = cursor.fetchall() #ler
for i in resultado:
    print(i)
# ********************************************************************


cursor.close() # fecha cursor
conexao.close() # fecha conexão
