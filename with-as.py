# -*- coding: UTF-8 -*-

#para nao precisar iniciar variável arquivo e fazer o bloco finally
with open('perfis.csv') as arquivo:
	for linha in arquivo:
		print linha