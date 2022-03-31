#   Exercício Python 069 - Estatísticas em produtos
#   Crie um programa que leia o nome e o preço de vários produtos.
#   O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#       A) qual é o total gasto na compra.
#       B) quantos produtos custam mais de R$1000.
#       C) qual é o nome do produto mais barato.

import numpy as numpy
#Espaços para armazenar as informações
bdpreco = []
bd1k = 0
produtonome = ''
menorvalor = 0
contador = 0

while True:
    print(f"-----Produto-----")
    #Insirir o valores de entrada
    produto = str(input(f"Digite o nome do produto: ")).lower()
    precoproduto = float(input(f"Digite o preço do produto: "))

    contador+=1

    opcao = str(input("Deseja continuar? Digite Sim ou Não: ")).lower()
    bdpreco.append(precoproduto)

    if precoproduto > 1000:
        bd1k+=1
    #se existir apenas um unico produto, ele sera o de menor valor
    # se o preco do novo produto for menor que o menor valor ja configurado na primeira
    # iteração, agora definir o novo valor como menor preco e definir o nome dele
    if contador == 1 or precoproduto < menorvalor:
        produtonome = produto
        menorvalor = precoproduto

    if opcao != 'sim':
        break
    else:
        continue

#mostrar isso na tela
print(f'''
Total gasto na compra: R${sum(bdpreco):.2f} 
Total de produtos que custam mais que mil reais: {bd1k}
o produto *{produtonome}* tem o menor valor sendo R${min(bdpreco)} 
''')
