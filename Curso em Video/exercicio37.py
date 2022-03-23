#   Exercício Python 037 - Conversor de Bases Numéricas
#   Escreva um programa em Python que leia um número inteiro qualquer
#   e peça para o usuário escolher qual será a base de conversão:
#   1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um valor: "))
opcao = int(input("Qual opção você deseja? "
                  "\n Digite 1 para converter em binario"
                  "\n Digite 2 para converter em octal" 
                  "\n Digite 3 para converter em hexadecimal\n"
                  "Escolha: "))

if opcao == 1:
    print(f"Resultado convertido em binario: {bin(num)}")
elif opcao == 2:
    print(f"Resultado convertido em octal: {oct(num)}")

elif opcao == 3:
    print(f"Resultado convertido em octal: {hex(num)}")

else:
    print("Não existe essa opção.")