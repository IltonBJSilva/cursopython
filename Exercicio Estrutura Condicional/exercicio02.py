'''
Cálculo do IMC (índice de massa corporal)
Faça um programa que solicite ao usuário seu nome, sexo, peso em kg (float) e sua altura
em metros (float) e calcule o IMC. A validação deve seguir a seguinte regra:
Condição IMC em Mulheres IMC em
Homens
abaixo do peso < 19,1 < 20,7
no peso normal 19,1 - 25,8 20,7 - 26,4
marginalmente acima do peso 25,8 - 27,3 26,4 - 27,8
acima do peso ideal 27,3 - 32,3 27,8 - 31,1
Obeso > 32,3 > 31,1
O resultado do programa deverá ser semelhante a este:
“Evaldo, com base no peso e altura informados, o IMC é imc e a condição é ‘condicao’.”
Onde imc é o cálculo obtido e condicao é uma das condições na tabela acima.
A equação para obter o imc é o peso em kg dividido pela altura em metros ao quadrado.
Desta forma:
'''

nome = input('Qual seu Nome: ')
sexo = input('Qual seu Genero: (M) ou (F): ')
peso = input('Qual seu Peso: ')
altura = input('Qual sua Altura: ')
imc = 0
condição = ''

nome = str(nome)
sexo = str(sexo)
condição = str(condição)
peso = float(peso)
altura = float(altura)
imc = float(imc)
imc = peso/(altura*altura)

if sexo == 'F' or sexo == 'f':
    if imc < 19.1:
        condicao = 'Abaixo do peso'
    elif 19.1 >= imc <= 25.8:
        condicao = 'Peso normal'
    elif 25.9 >= imc <= 27.3:
        condicao = 'marginalmente acima do peso'
    elif 27.4 >= imc <= 32.3:
        condicao = 'acima do peso ideal'
    elif imc > 32.4:
        condicao = 'Obeso'


elif sexo == 'M' or sexo == 'm':
    if imc < 20.7:

        condicao = 'Abaixo do peso'
    elif 20.8 >= imc <= 26.4:
        condicao = 'Peso normal'
    elif 26.5 >= imc <= 27.8:
        condicao = 'marginalmente acima do peso'
    elif 27.8 >= imc <= 31.1:
        condicao = 'acima do peso ideal'
    elif imc > 31.2:
        condicao = 'Obeso'
else:
    print("Invalido")

print(f'{nome}, com base no peso: {peso} e na altura: {altura} informados, o IMC é {imc} e a condição é {condicao}.')





