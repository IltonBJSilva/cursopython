#   Exercício Python 027 - Primeiro e último nome de uma pessoa
#   Faça um programa que leia o nome completo de uma pessoa
#   moastrando em seguido o primeiro e ultimo nome separadamente.

nome = str(input("Insira um nome: "))

print(f""""
Primeiro nome {nome.split()[0]}
Ultimo nome {nome.split()[-1]}
""")