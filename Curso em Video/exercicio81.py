#   Exercício Python 081 - Extraindo dados de uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#       A) Quantos números foram digitados.
#       B) A lista de valores, ordenada de forma decrescente.
#       C) Se o valor 5 foi digitado e está ou não na lista.

# take the second element for sort
def take_second(elem):
    return elem[1]


# random list
lista = list()

# sort list with key
sorted_list = sorted(lista, key=take_second)

# print list
print('Sorted list:', sorted_list)


