# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuários'
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprimir(self):
		  print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa)

class Data(object):
	'Classe de Data'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprimir(self):
		print '%s / %s / %s' %(self.dia, self.mes, self.ano)

class Pessoa(object):
	'Classe Pessoa para calcular o IMC'

	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def imprime_imc(self):
		imc = self.peso / (self.altura * self.altura)
		print 'Imc de %s: %s' %(self.nome, imc)