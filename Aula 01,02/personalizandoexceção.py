#Herda de Exception
class Error(Exception):
    pass
x = 0

#Herda da classe Error
#Sempre que fizer uma classe personalizada, vai precisar que herde de herror
class InputError(Error):
    #Construtor
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com um numero de 0 a 10: '))
        print(x)

        if x > 10:
            #Forçando uma exception
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')

        break
    except ValueError:
        print('Digite apenas numeros')
    except InputError as ex:
        print(ex)

