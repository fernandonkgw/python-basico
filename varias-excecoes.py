# -*- coding: UTF-8 -*-

from models import *
arquivo = None #inicializa a variável
try:
	arquivo = open('perfis.csv','r')
	valores = arquivo.readline().split(',') #deveria ser vírgula
	Perfil(*valores)
except IOError as erro:
	print 'Deu IOError %s' % erro
except TypeError as erro:
	print 'Deu TypeError %s' % erro
finally:
	if(arquivo is not None):
		print 'fechando arquivo'
		arquivo.close()