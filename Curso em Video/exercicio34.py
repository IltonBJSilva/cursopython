#   Exercício Python 034 - Aumentos múltiplos
#   Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#   Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salario do funcionario: R$"))

if salario > 1250:
    reajuste = salario+((salario*(10/100)))
    print(f'Novo Salario: R${reajuste:.2f}')

elif salario < 1250:
    reajuste = salario+((salario*(15/100)))
    print(f'Novo Salario: R${reajuste:.2f}')

else:
    print("Erro 404")