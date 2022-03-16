#   Exercício Python 024 - Verificando as primeiras letras de um texto
#   Faça um programa que leia o nome de uma cidade
#   e diga se ela começa ou não com o nome "Santos"

cidade = str(input("Digitei o nome da cidade: "))

if cidade.split()[0].find('Santos'):
    print("Não começa com Santos")
else:
    print("Começa com Santos")



