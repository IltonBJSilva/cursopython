from functools import reduce
from importlib.metadata import unique_everseen
from operator import mul

import duplicates as duplicates

lista = []
lista_repete = []
lista_unica = []

while True:
    numeros = int(input("Informe os números (número zero para sair): "))

    def remove_repetidos(lista):
        lista_numeros_unicos = []
        for numeros in lista:
            if numeros not in lista_numeros_unicos:  # Verifica se o atual elemento existe na lista original
                lista_numeros_unicos.append(numeros)  # Se não existir, adiciona com o comando append() o numero na lista
        return lista_numeros_unicos
    if numeros == 0:
        break
    lista.append(numeros)

for posicao in lista:
    if posicao not in lista_unica:
        lista_unica.append(posicao)
    else:
        if posicao not in lista_repete:
            lista_repete.append(posicao)

print("Lista: ",lista,"\n")
print("Lista Unica sem repetição: ",remove_repetidos(lista),"\n")
print("Numeros Repetidos: ",lista_repete,"\n")