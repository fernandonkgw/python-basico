# -*- coding: UTF-8 -*-
try:
	arquivo = open('nao-existe.txt','r')
	print('O arquivo foi aberto')
	arquivo.close()
except IOError as erro:
	print 'Deu IOError: %s' % erro