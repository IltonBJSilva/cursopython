#   Exercício Python 022 - Analisador de Textos
#   Crie um programa que leia o nome completo de uma pessoa e mostre:
#       - O nome com todas as letras maiúsculas e minúsculas.
#       - Quantas letras ao todo (sem considerar espaços).
#       - Quantas letras tem o primeiro nome.

import re

nome = str(input("Inisra o nome: "))

print(f"""
Nome Maiúsculo: {nome.upper()}
Nome Minúsculo: {nome.lower()}
Quantidade de letra: {len(re.sub(' ','',nome))}
Quantidade de letra do primeiro nome: {len(nome.split()[0])}
""")