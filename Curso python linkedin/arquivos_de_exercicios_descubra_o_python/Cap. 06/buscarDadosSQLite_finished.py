# 
# Exemplo de acesso a uma base de dados SQLite
#

import sqlite3

#Função para permitir que informe o banco de dados e o comando
def manipulaDados(bancoDados, comando):
    #Objeto que faz conexão com o banco de dados
    conexao = sqlite3.connect(bancoDados)
    #Criar um curso responsavel pela execusão do comando
    cursor = conexao.cursor()
    #Executando um comando
    cursor.execute(comando)
    #Efetivar as alterações
    conexao.commit()
    #Fechar a conexão com o sqlite
    conexao.close()

#Criar uma função para fazer o comando de select no banco de dados
def selecionaDados(bancoDados, comando):
    #Conexão com o banco de dados
    conexao = sqlite3.connect(bancoDados)
    #Cursos para manipulação do arquivo
    cursor = conexao.cursor()
    #Executando o comando
    cursor.execute(comando)
    #Comando
    linhas = cursor.fetchall() #função para buscar todas as linhas retornadas pelo comando
    #Para exibir todas as linhas de uma tabela
    for linha in linhas:
        print(linha)

#Criar uma função para executar
def ManipulacaoDados():
    #Comando insert
    comandoInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado Teste', 'XX', 'Teste Inclusão')"
    #O path do banco de dados, local onde esta
    pathBD = "F:\\Projetos Python\\cursopython\\Curso python linkedin\\arquivos_de_exercicios_descubra_o_python\\Cap. 06\\BancoDeDados.db"
    #Criar comando apra mostrar
    comandoSELECT = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    #Para incluir informação ao banco de dados
    manipulaDados(pathBD, comandoInsert)
    #Para verificar se foi feita com sucesso, mostrar
    selecionaDados(pathBD, comandoSELECT)

ManipulacaoDados()