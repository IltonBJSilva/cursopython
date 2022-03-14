#   Exercício Python 004 - Dissecando uma Variável
#   Faça um programa que leia algo pelo teclado
#   e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = str(input("Digite algo: "))
print(frase.title())

print(f"O tipo primitivo desse valor é {type(frase)}")
print(f"Só tem espaços? {frase.isspace()}")
print(f"É um número? {frase.isnumeric()}")
print(f"É alfabético? {frase.isalpha()}")
print(f"É alfanumérico? {frase.isalnum()}")
print(f"Esta em maiúsculas? {frase.isupper()}")
print(f"Esta em minúsculas? {frase.islower()}")
print(f"Esta capilatizado? ou seja, cada palavra começa com uma letra maiuscula {frase.istitle()}")