lista = [1,10]

arquivo = open('testador.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
    print('Fechando arquivo')

except ZeroDivisionError:
    print('Impossivel ser dividido')
except IndexError:
    print('Erro Index')
except BaseException as ex:
    print(f'Erro desconhecido: {ex}')
else:
    print('EXECUTADO')

finally:
    print('Sempre executa')
    arquivo.close()
