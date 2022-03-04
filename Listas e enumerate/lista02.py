lista = [10.2, 13.75, 17.58, ["Maçã", "Banana", "Abacaxi"]]

print(lista)
#Resultado: [10.2, 13.75, 17.58, ['Maçã', 'Banana', 'Abacaxi’]]
frutas = lista[3]


print(frutas)
'''
Assim print(frutas) ou print(frutas[0]) na segunda opção
se referencia por indice, ou seja vai aparecer apenas um dos resultados a cima da lista dentro
da outra lista

'''
#Resultado: ['Maçã', 'Banana', 'Abacaxi’]
soma = lista[0] + lista[1] + lista[2]

print(soma)
#Resultado: 41.53