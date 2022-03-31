#   Exercício Python 067 - Tabuada v3.0
#   Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#   O programa será interrompido quando o número solicitado for negativo.



while True:
    tabuada = int(input("Qual tabuada deseja saber?\n Digite: "))

    if tabuada == 0:
        print('-'*10)
        print("Fechado")
        print('-'*10)
        break

    for n in range (1,11):
        resposta = n*tabuada
        print(f" {tabuada} x {n} = {resposta}")
