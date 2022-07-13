# 
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom

def manipulaXML():
	doc = xml.dom.minidom.parse("F:\\Projetos Python\\cursopython\\Curso python linkedin\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemploXML.xml")
	print("Nome da primeira tag: ", str(doc.firstChild.tagName))
	primeiroNome = doc.getElementsByTagName("firstname")
	print(f"Primeiro nome: {primeiroNome[0].firstChild.nodeValue}")

	for skill in doc.getElementsByTagName("skill"):
		print(f"Skill encontrada: ",skill.getAttribute("name"))


manipulaXML()