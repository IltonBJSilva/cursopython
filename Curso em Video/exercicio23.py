#   Exercício Python 023 - Separando dígitos de um número
#   Faça um programa que leia um número de 0 a 9999
#   e mostre na tela cada um dos dígitos separados.

numero = int(input("Digite um numero: "))

n = str(numero)

if 0 <= numero <= 99:
    print(f'''
    Dezena: {n[0]}
    Unidade: {n[1]}
    ''')

elif 100 <= numero <= 999:
    print(f'''
    Centena: {n[0]}
    Dezena: {n[1]}
    Unidade: {n[2]}
    
    ''')

elif 1000 <= numero <= 9999:
    print(f'''
    Milar: {n[0]}
    Centena: {n[1]}
    Dezena: {n[2]}
    Unidade: {n[3]}
    ''')