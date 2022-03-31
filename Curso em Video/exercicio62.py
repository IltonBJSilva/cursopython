#   Exercício Python 062 - Super Progressão Aritmética v3.0
#   Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#   Oprograma encerrará quando ele disser que quer mostrar 0 termos.

ptermo = int(input("Digite o primeiro termo da progressão PA: "))
razao = int(input("Digite a razão da progressão PA: "))
opcao = int(input("Deseja mostrar quantos termos: "))

contador = 1;
while contador != opcao:
    if opcao == 0:
        print("Finalizado")
        break
    else:
        contador += 1
        an = ptermo + (contador - 1) * razao
        print(f' {an} ', end='->')

print("ACABOU!!")