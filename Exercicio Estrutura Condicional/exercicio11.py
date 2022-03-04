tabuada = input("Qual tabuada deseja saber?\n Digite: ")
tabuada = int(tabuada)

for n in range (1,11):
    resposta = n*tabuada
    print(tabuada, 'x', n, '=', resposta)
