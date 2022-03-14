#   Exercício Python 013 - Reajuste Salarial
#   Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

aumento = 15
salario = float(input("Digite o salario do funcionario para saber o aumento: "))


salarioFinal = salario+(salario*(aumento/100))


print(f"Salario atual e de: {salarioFinal:.2f}")