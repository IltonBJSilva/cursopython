#   Exercício Python 70 - Jogo do Par ou Ímpar
#   Crie um programa que leia a idade e o sexo de várias pessoas.
#   A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#       A) quantas pessoas tem mais de 18 anos.
#       B) quantos homens foram cadastrados.
#       C) quantas mulheres tem menos de 20 anos

#Espaços para armazenar as informações
quantwoman = 0
maiores = 0
quantman = 0

while True:
    print(f"-----Produto-----")
    #Insirir o valores de entrada
    sexo = str(input(f"Digite [M] ou [F]: ")).lower()
    idade = int(input(f"Qual sua idade: "))
    opcao = str(input("Deseja continuar? Digite Sim ou Não: ")).lower()


    if idade >= 18:
        maiores+=1

    if sexo == 'm':
        quantman+=1

    if sexo == 'f' and idade < 20:
        quantwoman+=1


    if opcao != 'sim':
        break
    else:
        continue

print(f'''

Quantidade de pessoas que são maiores de 18: {maiores}
Foram cadastro ao todo {quantman} de homens
Possui {quantwoman} de mulheres com menos de 20 anos de idade
''')