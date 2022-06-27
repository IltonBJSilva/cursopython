
conjunto = {1,2,3,4}
conjunto2 = {4,5,6,7,8}

#unir 2 conjuntos
uniao = conjunto.union(conjunto2)

#interseção, oque tem tanto no primeiro conjunto quanto no segundo conjunto
intersecao = conjunto.intersection(conjunto2)

#Diferença, oque tem no primeiro, porem não tem no segundo
diferenca = conjunto.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto)

#Diferença simetrica
simetrica = conjunto.symmetric_difference(conjunto2)

'''
#adicionar
conjunto.add(5)
#Remover
conjunto.discard(2)
'''




print(f'União {uniao}')
print(f'Inteseção {intersecao}')
print(f'Diferença entre o conjunto 1 e 2{diferenca}')
print(f'Diferença entre o conjunto 2 e 1{diferenca2}')

print(f'Diferença simetrica {simetrica}')





