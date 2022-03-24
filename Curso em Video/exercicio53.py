#   Exercício Python 053 - Detector de Palíndromo
#   Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
txt = str(input("Saiba e um polindromo: ")).split()
s = ""
s = s.join(txt)
if s[::-1].lower() == s.lower():
    print(f'{txt} - E um palindromo')
else:
    print("Não e um palindromo")