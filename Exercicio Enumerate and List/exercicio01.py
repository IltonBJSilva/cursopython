from functools import reduce
from operator import mul
lista_numero = []
while True:
    quantidade = int(input("Informe um número (número zero para sair): "))
    if quantidade != 0:
        lista_numero.append(quantidade)
        #Soma da lista
        soma = sum(lista_numero)
        #multiplicação da lista
        mult = reduce(mul, lista_numero,1)
        #Maior valor de uma lista
        max_value = max(lista_numero)
        #Menor valor de uma lista
        min_value = min(lista_numero)
    elif quantidade == 0:
        break
for posicao, numero in enumerate(lista_numero, start=1):
    print(f"#{posicao} - {numero}")
print(f'Soma total:{soma} \n Multiplicação Total:{mult} \n Valor Maximo:{max_value} \n Valor Minimo:{min_value}')
