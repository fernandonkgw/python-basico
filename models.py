# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuários'
	def __init__(self, nome, telefone, empresa):

		if(len(nome) < 3):
			raise Argumento_Invalido_Error('Nome deve ter pelo menos 3 caracteres')

		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo,'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')

			if(len(valores) is not 3):
				raise Perfil_Error('Uma linha no arquivfo %s deve ter 3 valores' % nome_arquivo)

			perfis.append(classe(*valores))
		arquivo.close()
		return perfis

class Perfil_Vip(Perfil):
	'Classe para perfil de usuários vips'
	def __init__(self, nome, telefone, empresa, apelido=''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0

class Argumento_Invalido_Error(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)

class Perfil_Error(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)

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

class Retangulo(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area

class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def calcular_imposto(self): 
        self.saldo = self.saldo * 0.10
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, titular, saldo):
        super(ContaCorrente, self).__init__(titular, saldo)

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20