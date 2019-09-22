import os
import pandas as pd
import statistics
from math import *

def procura_arquivos():
	DIRETORIO = 'dados/'
	lista_arquivos = []
	for _, _, arquivo in os.walk(DIRETORIO):
		lista_arquivos.append(arquivo)
	return lista_arquivos

def le_arquivo():
	with open("dados/dados_sinal_normal_completo16.csv", 'r') as f:
		return pd.read_csv(f, sep=',').drop('disturbio', axis=1)

def desvio_medio(linhas):
	desvio_medio = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		media = statistics.mean(linha)
		for i in range(0, N):
			soma += abs(linha[i] - media)
		desvio_medio.append(soma/N)

	return desvio_medio

def media_harmonica(linhas):
	media_harmonica = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		for i in range(0, N):
			soma += (1/linha[i])
		media_harmonica.append(N/soma)

	return media_harmonica

def desvio_padrao(linhas):
	desvio_padrao = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		media = statistics.mean(linha)
		for i in range(0, N):
			soma += ((linha[i] - media)**2)
		desvio_padrao.append(sqrt(soma / (N - 1)))

	return desvio_padrao

def skewness(linhas, desvio_padrao):
	skewness = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		media = statistics.mean(linha)
		for i in range(0, N):
			soma += ((linha[i] - media) ** 3)
		skewness.append(soma / (N * (desvio_padrao[i] ** 3) ))

	return skewness

def kurtosis(linhas):
	kurtosis = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma_2 = 0
		soma_4 = 0
		media = statistics.mean(linha)
		for i in range(0, N):
			soma_4 += ((linha[i] - media) ** 4)
			soma_2 += ((linha[i] - media) ** 2)
		soma_4 *= (1 / N)
		soma_2 *= (1 / N)
		kurtosis.append(soma_4 /(soma_2 ** 2))

	return kurtosis

def entropia_renyi(linhas, alfa=0.6):
	entropia_renyi = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		for i in range(0, N):
			soma += (linha[i] ** alfa)
		soma = (1 / (1 - alfa)) * log10(soma)
		entropia_renyi.append(soma)
	return entropia_renyi

def entropia_shannon(linhas):
	entropia_shannon = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		for i in range(0, N):
			soma += ((linha[i] ** 2) * log10((linha[i]) ** 2))
		soma *= -1
		entropia_shannon.append(soma)
	return entropia_shannon

def dif(linhas):
	dif = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		dif.append(max(linha) - min(linha))
	return dif

def pico(linhas):
	pico = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		pico.append(max(linha))
	return pico

def rms(linhas):
	rms = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		N = len(linha)
		soma = 0
		for i in range(0, N):
			soma += abs(linha[i])
		soma = sqrt((1 / N) * soma)
		rms.append(soma)
	return rms

def fator_crista(linhas, pico, rms):
	fator_crista = []
	for i, row in linhas.iterrows():
		fator_crista.append(pico[i] / rms[i])
	return fator_crista

def fator_forma(linhas, rms):
	fator_forma = []
	for i, row in linhas.iterrows():
		linha = list(row.array)
		media = statistics.mean(linha)
		fator_forma.append(media / rms[i])
	return fator_forma

linhas = le_arquivo()
media_harmonica = media_harmonica(linhas)
desvio_medio = desvio_medio(linhas)
desvio_padrao = desvio_padrao(linhas)
skewness = skewness(linhas, desvio_padrao)
kurtosis = kurtosis(linhas)
entropia_renyi = entropia_renyi(linhas)
entropia_shannon = entropia_shannon(linhas)
dif = dif(linhas)
pico = pico(linhas)
rms = rms(linhas)
fator_crista = fator_crista(linhas, pico, rms)
fator_forma = fator_forma(linhas, rms)