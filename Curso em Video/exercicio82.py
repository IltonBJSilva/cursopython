#   Exercício Python 082 - Valores únicos em uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista.
#   Depois disso, crie duas listas extras que vão conter apenas os valores pares e
#   os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numeros = list()
impar = list()
par = list()
while True:
    entrada = int(input('Digite:'))
    numeros.append(entrada)
    if entrada % 2 == 0:
        par.append(entrada)
    else:
        impar.append(entrada)
    sair = int(input("Digite 1 para sair: "))
    if sair == 1:
        break
print(f'''Lista de todos os valores geral: {numeros}\n Lista de todos os valores impar: {impar}\n Lista de todos os valores par:   {par}''')