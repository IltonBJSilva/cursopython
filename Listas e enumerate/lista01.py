'''
# Criando uma lista com 3 inteiros
lista_numeros = [54, 23, 12]

# Será impresso 78, os elemetos da lista iniciam com zero
# 0=54, 1=23, 2=12
# Na linha abaixo será impresso 23
print(lista_numeros[1])

# Alterando o segundo elemento da lista de 54 para 90
lista_numeros[1] = 90

# Na linha abaixo será impresso 90
print(lista_numeros[1])

# Acessando os elementos para calcular a média
notas = [7.5, 5.6, 9.5, 10.0]
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print(media)
'''

banco = ['Itau','Santander','Inter','Nubank']

#for numero in banco:
    #print(numero,"",end='')


linguagens = ["Python", "Cobol", "Clipper", "C", "C++", "Go", "JavaScript"]
print(linguagens)
del linguagens[0] # Removeu JavaScript
print(linguagens)
#Primeiro valor e onde começa e o ultimo e onde para, se for 1:4 vai começar em cobol e terminar em C, não conta o 4
del linguagens[1:4] # Removeu Cobol e Clipper
print(linguagens)
