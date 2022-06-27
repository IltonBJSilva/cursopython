class Calculadora:
    #sempre que instanciar a classe calculadora, vai passar pela classe init, não vai passar pelo soma antes do init
    #sem utilizar o init, e pode apagar o init e vai rodar normal
    def __init__(self):
        pass

    def soma(self,valor_a,valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a,valor_b):
        return valor_a - valor_b

    def multiplica(self,valor_a,valor_b):
        return valor_a * valor_b

    def divisao(self,valor_a,valor_b):
        return valor_a / valor_b


#instanciar a classe
calculadora = Calculadora()



#chamar a função
print(calculadora.soma(10,5))
print(calculadora.multiplica(2,5))
print(calculadora.subtracao(2,2))
print(calculadora.divisao(10,2))





