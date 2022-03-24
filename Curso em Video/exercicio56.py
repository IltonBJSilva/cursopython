#   Exercício Python 056 - Analisador completo
#   Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#   No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
#   e quantas mulheres têm menos de 20 anos.
import numpy as numpy
#Espaços para armazenar as informações
soma_idade = 0
homem_idade = 0
homem_nome = ''
c_mulheres = 0


for x in range(1,5):
    print(f"----- {x}º Pessoa -----")
    #Insirir o valores de entrada
    nome = str(input(f"Digite seu nome: ")).lower()
    idade = int(input(f"Digite sua idade: "))
    sexo = str(input("Sexo [M/F]: ")).lower()
    soma_idade += idade

    #Comparação para saber em qual iteração teve a maior idade e o nome do homem
    if sexo.lower() in 'm' and idade > homem_idade:

        homem_idade = idade
        homem_nome = nome

    #Comparação para saber quantas mulheres tem menos de 20 anos de idadde
    if sexo.lower() in 'f' and idade < 20:
        c_mulheres += 1


#mostrar isso na tela
print(f"A média de idade do grupo é de {soma_idade / 4:.1f}")
print(f"O homem mais velho tem {homem_idade} anos e se chama {homem_nome}")
print(f"Ao todo são {c_mulheres} mulheres com menos de 20 anos")

