# 
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser
import json
import urllib.request

class meuParse(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Tag de abertou encontrada")
		if attrs.__len__() > 0:
			for a in attrs:
				print("  Valores encontrados: ",a[0], " = ",a[1])

	def handle_endtag(self,tag):
		print("Tag de fechamento encontrada")

	def handle_comment(self, str):
		print("Comentario encontrado.")

	def handle_data(self, data):
		print("Valores encontrados.")
		if data.isspace():

			print("O valor encontrado e um espaço.")
		else:
			print("O valor encontrado é: ", data)

def meuObjeto():
	meuparse1 = meuParse()
	arquivo = open("F:\\Projetos Python\\cursopython\\Curso python linkedin\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemplohtml.html","r")
	dados = arquivo.read()
	meuparse1.feed(dados)


meuObjeto()