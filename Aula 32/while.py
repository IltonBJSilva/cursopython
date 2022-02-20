'''
while True:
    nome = input("Teu nome meu fi: ")
    print(f'Olá {nome}')



#Pula o numero 3
x = 0
while x < 10:
    if x == 3:
        x=x+1
        continue
    print(x)
    x=x+1

#x decrecente
#y crescente
x = 11
y = 0

while x <= 11:
    while y < 10:
        y+=1
        x-=1
        print(f'Valor de x = {x} e de Y = {y}')


x = 0 #coluna
while x < 10:

    y = 0 #linha

    while y < 5:
        print(f'({x}),({y})fx')
        y+=1
    x+=1
'''

while True:
    print()
    num_1 = input("Digite um valor: ")
    num_2 = input("Digite um valor: ")
    operador = input("Digite um operador\n + para soma\n - para subtrair\n / para dividir\n Digite o operador: ")
    sair = input("Deseja sair? sim [s] ou não [n]")

    #Validação se o usuario deseja sair.

    if sair == "s":
        break

    #Validação para que seja digitado apenas numero
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)


    if operador == "+":
        resultado = num_1+num_2
        print(f"Resultado da adição:{resultado}")

    elif operador == "-":
        resultado = num_1-num_2
        print(f"Resultado da subtração:{resultado}")

    elif operador == "/":
        resultado = num_1/num_2
        print(f"Resultado da divisão:{resultado:.2f}")

    else:
        print("Invalido")




