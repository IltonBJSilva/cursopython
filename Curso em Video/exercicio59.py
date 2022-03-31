#   Exercício Python 058 - Jogo da Adivinhação v2.0
#   Crie um programa que leia dois valores e mostre um menu na tela:
#       [ 1 ] somar
#       [ 2 ] multiplicar
#       [ 3 ] maior
#       [ 4 ] novos números
#       [ 5 ] sair do programa
#   Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    valor1 = int(input("Insira o primeiro valor: "))
    valor2 = int(input("Insira o segundo valor: "))
    opcao = int(input('''
    Escolha qual opção deseja
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Escolha: '''))
    if opcao == 1:
        soma = valor1+valor2
        print(f"Soma = {soma}")

    elif opcao == 2:
        mult = valor1*valor2
        print(f"Multiplicação = {mult}")
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print(f"Maior valor {maior}")
        else:
            maior = valor2
            print(f"Maior valor {maior}")

    elif opcao == 4:
        continue
    elif opcao == 5:
        break
    else:
        print("Opção invalida")





