#   Exercício Python 080 - Lista ordenada sem repetições
#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#   já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = list()

for intervalo in range(0, 5):
    entrada = int(input("Digite um valor: "))

    #para ordernar na primeira posição e ficar em sequencia
    if intervalo == 0 or entrada > lista[-1]:
        #inserir na lista
        lista.append(entrada)
        print(f'O valor {entrada} foi adicionado na última posição')


    #Caso o valor inserido seja maior que o menor valor da lista
    else:
        validar = 0
        #validar o tamanho da lista para não ultrapassar de 5
        while validar < len(lista):
            #durante o while percorrer, vai validar se na posição na iteração, o valor e menor ou igual ao de entrada
            if entrada <= lista[validar]:
                #inserir a variavel de entrada na posição validar
                lista.insert(validar,entrada)
                print(f'O valor {entrada} foi adicionado na posição {validar}')
                break
            validar += 1





print(f'Valores digitados: {lista}')
