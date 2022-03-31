#   Exercício Python 061 - Progressão Aritmética v2.0
#   Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#   mostrando os 10 primeiros termos da progressão usando a estrutura while.
ptermo = int(input("Digite o primeiro termo da progressão PA: "))
razao = int(input("Digite a razão da progressão PA: "))

contador = 1;
while contador != 10:
    contador += 1
    an = ptermo+(contador-1)*razao
    print(f' {an} ',end='->')
print("ACABOU!!")


