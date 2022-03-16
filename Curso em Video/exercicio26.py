#   Exercício Python 026 - Primeira e última ocorrência de uma string
#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

frase = str(input("Digite uma frase: "))

print(f'''
Quantidade de Letra A: {frase.count('A')}
Posição que a letra aparece pela primeira vez: {frase.find('A')+1}
Posição que a letra aparece pela ultima vez: {frase.rfind('A')}

''')