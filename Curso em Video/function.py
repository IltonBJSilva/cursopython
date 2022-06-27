class Calculadora:
    #sempre que instanciar a classe calculadora, vai passar pela classe init, não vai passar pelo soma antes do init
    def __init__(self, num1, num2):
        #self e para referenciar o proprio objetoi
        self.valor_a = num1
        self.valor_b =  num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplica(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


#instanciar a classe
calculadora = Calculadora(10,2)

#acessar os valores
print(calculadora.valor_a)
print(calculadora.valor_b)

#chamar a função
print(calculadora.soma())
print(calculadora.multiplica())
print(calculadora.subtracao())
print(calculadora.divisao())





