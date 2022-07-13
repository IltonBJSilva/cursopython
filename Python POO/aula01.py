#criando uma classe seguindo esse padrão de nome com nome Maiusculo e minisculos
class Usuario:
	#não e um atributo de instancia mais
	cargo = 'usuario'
	#Comparando com Java, seria um construtor
	def __init__(self, nome,idade,altura):
		self.altura = altura

	#Decorador em cima de um metodo afirma para o compilador
	#Que não e mais um metodo de instancia,
	@classmethod
	def cargo_usuario(cls):
		cls.cargo = "Gerente"
		print(cls.cargo)


Usuario.cargo_usuario()