#criando uma classe seguindo esse padrão de nome com nome Maiusculo e minisculos
class Usuario:
	#não e um atributo de instancia mais
	cargo = 'usuario'
	#Comparando com Java, seria um construtor
	def __init__(self, nome,idade,altura):
		self.altura = altura

	#Não acessa os atributos de instancia e nem de classe
	@staticmethod
	def e_adulto(idade):
		if idade >= 18:
			print(True)
		else:
			print(False)

#Precisa de um paramentro
Usuario.e_adulto(20)