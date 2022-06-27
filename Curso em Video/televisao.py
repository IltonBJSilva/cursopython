class Televisao:
    def __init__(self):
        #sempre que instanciar, ela vao começar desligada
        self.ligada = False
        self.canal = 5

    def power(self):
        #if em variavel Boolean ja vai entender a opção oposto
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada: #vai comparar com o oposto
            self.canal += 1
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':

    televisao = Televisao()
    print(f'Televisão Desligada: {televisao.ligada}')
    televisao.power()
    print(f'Televisão Ligada: {televisao.ligada}')
    televisao.power()
    print(f'Televisão Desligada: {televisao.ligada}')

    print(f'Canal: {televisao.canal}')
    televisao.power()
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(f'Aumenta Canal: {televisao.canal}')
    televisao.diminui_canal()
    print(f'Diminui Canal: {televisao.canal}')
