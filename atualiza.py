#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Descricao: Notificacao de atualizacao da pagina do professor via Telegram
# Autor: Joahannes Costa
# Data: 14.05.2018

import os
import sys
import time

import requests

def copy_page():

	path = "/home/joahannes/bot/"
	idbot = "https://integram.org/webhook/cHnEjEDNd2R"

	#Modificado para curl dir
	page = sys.argv[1] #"https://www.ic.unicamp.br/~lee/mo417/"

	arquivo = 'pg1.txt'
	comando1 = 'curl ' + str(page) + ' > ' + str(path) + str(arquivo)
	os.system(comando1)

	#Verificando atualizacoes
	comando2 = "diff " + str(path) + "pg.txt " + str(path) + "pg1.txt"
	retorno = os.system(comando2)

	#print "Retorno:", retorno

	if retorno == 0:
	 	#Sem atualizacoes na pagina
	 	#remove arquivo de comparacao
	 	os.system('rm ' + str(path) + 'pg1.txt')
	else:
		#Pagina atualizada
		#Removendo pg.txt antigo
	 	os.system('rm ' + str(path) + 'pg.txt')
	 	#Atualizando pg.txt
	 	os.system('mv ' + str(path) + 'pg1.txt ' + str(path) + 'pg.txt')
	 	#Enviando notificacao para bot
	 	#cURL
	 	headers = {
	 		'Content-Type': 'application/json',
	 	}
	 	data = '{"text":"LEE-MO417: Pagina ATUALIZADA!"}'
	 	response = requests.post(idbot, headers=headers, data=data)


if __name__ == "__main__":
	pass
	copy_page()