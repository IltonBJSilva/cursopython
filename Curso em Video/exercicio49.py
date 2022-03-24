#   Exercício Python 049 - Tabuada v.2.0
#   Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = input("Qual tabuada deseja saber?\n Digite: ")
tabuada = int(tabuada)

for n in range (1,11):
    resposta = n*tabuada
    print(f" {tabuada} x {n} = {resposta}")

