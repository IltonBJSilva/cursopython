#   Exercício Python 072 - Número por Extenso
#   Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#   Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)

pos = -1
while True:
    pos = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[pos]}')

    opcao = str(input("Deseja sair? Sim[S] - Não[N] \nQual: ")).lower()

    if opcao == 'sim' or pos < 0 or pos > 20:
        break






