    #   Exercício Python 064 - Progressão Aritmética v2.0
#   Crie um programa que leia vários números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#   No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
bd = []
print('-'*100)
print(
'''Caso deseje parar, digite '999' caso contrario todo numero digitado vai ser incluido em nosso
banco de dados e sera computado e uma grande soma de valores com exceção da condição de parar.''')
print('-'*100)
while True:
    valor = int(input("Digite: "))
    if valor == 999:
        break

    bd.append(valor)


print(f'''
Soma total de valores - {sum(bd)}
Quantidade de numeros - {bd}

''')