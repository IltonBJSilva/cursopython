"Entada de dados"
'''
nome = str(input("Qual o seu nome? \n"))
idade = int(input("Qual sua idade? \n"))
'''

escolha = str(input("Escolha a operação\n + para soma\n - para subtração\n"))

print("Pronto, escolha os valores")
numero_1 = int(input("Digite um valor \n"))
numero_2 = int(input("Digite um valor \n"))

if escolha == "+":
    resultado = numero_1+numero_2
    print(resultado)

elif escolha == "-":
    resultado = numero_1-numero_2
    print(resultado)

else:
    print("Valor incorreto")


#ano_atual=2022

#nascimento = ano_atual-int(idade)

#print(f'Seu nome é: {nome} e nasceu em {nascimento}')

