#   Exercício Python 057 - Validação de Dados
#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    genero = str(input("Insira qual seu genero apenas e aceito esses --> 'M' ou 'F'. \nEscolha: "))
    if genero ==  'M' or genero == 'F':
        print("Sucesso")
        break
    else:
        print("Errado")

