'''
Formatação e divisão de valores
'''
num_1 = 10
num_2 = 3

divisao = num_1 / num_2

#Mostra um resultado de 3.3333333333333335
#print( '{}'.format(divisao) )

#Mostra um resultado de 3.33
#:.2f você escolhe a quantidade de numero de pontos flutuantes
#print( '{:.2f}'.format(divisao) )

#Usando F-String
#print(f'{divisao:.2f}')
'''''
nome = 'Ilton Batista'

print(f'{nome:s}')
'''

'''
:(Caractere) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

num_1 = 1
print(f'{num_1:0>10}')
#Resultado: 0000000001

num_2 = 1
print(f'\n{num_1:0<10}')
#Resultado: 1000000000

num_3 = 1
print(f'\n{num_1:0^10}')
#Resultado: 0000100000

num_4 = 1
print(f'\n{num_1:0>10.2f}')
#Resultado: 0000001.00


nome = "Ilton Batista"
print(f'\n{nome:#^50}')
#Resultado: ##################Ilton Batista###################

#Formatação fora do print
nome = "Ilton Batista"
nome_formatado = '{n:#>20}'.format(n=nome)
print(nome_formatado)
#Resultado: #######Ilton Batista
'''

#Formatação fora do print com sobrenome conseguindo formatar cada um unicamente
nome = "Ilton"
sobrenome = 'Batista'
nome_formatado = '{0:#>20}{1:$<20}'.format(nome, sobrenome)
print(nome_formatado)
#Resultado: ###############IltonBatista$$$$$$$$$$$$$