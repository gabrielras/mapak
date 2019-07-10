import pandas as pd
from KaranoughtAlgorithm import kreader8
from Kreader4 import Kreader4
from KaranoughtAlgorithm import kcreator 
from BotGeradordeTabela import BotGeradorDeTabela
from leitor import leitor
from leitor3 import leitor3
bot = BotGeradorDeTabela()
equationreader3 = leitor3()
reader = kreader8.kreader8
reader4=Kreader4()
equationreader = leitor()
choice = int(input())
counter = int(0)
#Caso o cara queira digitar a equação
if choice ==1:
	nVariaveis = int(input())#Aqui entra as variáveis.
	equation = input()#Aqui entra a equação
	entradasTabela = equationreader3.leitordaequacao(nVariaveis,equation)
	tabelaverdade = pd.DataFrame(entradasTabela)
	valorX = tabelaverdade.iloc[:][nVariaveis].values
	print(tabelaverdade)
#Caso o cara queira digitar a tabela verdade
else:
	print("Aqui vai entrar a tabela verdade,tu precisa passar ela aqui")
	#tabelaverdade = #Como eu faço para receber?	
	'''
	#Loop simulador da putaria.
	i =0
	while i!=100:
		reader = kreader8.kreader8
		i = int(i+1)
		reader4=Kreader4()
		nVariaveis = bot.choiceCreator()
		print("O bot escolheu:",nVariaveis," variaveis")
		valorX=bot.createTabelaVerdade(2**nVariaveis)
		reader2 = kcreator.MapaK
		matriz = reader2.MapaCreator(valorX,nVariaveis)
		mapaK = pd.DataFrame(matriz)#Aqui ta o mapa de Karnought.
		print("Olha ae o mapak")
		print(mapaK)
		if nVariaveis == 3:
			reader.mapaK(reader,valorX,nVariaveis,1)
			equacao = reader.interpretador(reader,1)
			if(equacao!='1'and equacao!='0'): 
				equisimplificada = ''.join(equacao)#ESta aqui é a equação simplificada.
				entradasTabela = equationreader3.leitordaequacao(nVariaveis,equisimplificada)
				print("Equação simplificada")
				print(equisimplificada)
				entradasTabela = equationreader3.leitordaequacao(nVariaveis,equisimplificada)
				tabelaverdade = pd.DataFrame(entradasTabela)
				print("Tabela verdade")
				print(tabelaverdade)
				bateu = False 
				print("OLHA AQUI",tabelaverdade.iloc[0][nVariaveis])
				for i in range(1,len(valorX)):
					if valorX[i]!=tabelaverdade.iloc[i][nVariaveis]:
						bateu = True
				if(bateu==True):
					f= open("testandocodigo.txt","a")
					f.write(equisimplificada+"\r\n")
					f.close()
					#del equisimplificada[:]
		if nVariaveis == 4:
			reader4.karnaught(valorX,nVariaveis,1)
			if(reader4.agrupamento4x4==2):
				equisimplificada = ''.join(reader4.printer())
				print("Equação simplificada")
				print(equisimplificada)
				entradasTabela = equationreader3.leitordaequacao(nVariaveis,equisimplificada)
				tabelaverdade = pd.DataFrame(entradasTabela)
				bateu = False 
				for i in range(1,len(valorX)):
					if valorX[i]!=tabelaverdade.iloc[i][nVariaveis]:
						bateu = True
				if(bateu==True):
					counter = int(0)
					f= open("testandocodigo.txt","a")
					f.write(equisimplificada+"\r\n")
					f.close()
			else:
				print(reader4.agrupamento4x4)
		
	'''
	#print("Quantas vezes falhou nosso código:",counter)
#print(valorX)
#Aqui esta as saídas do circuito
reader2 = kcreator.MapaK
matriz = reader2.MapaCreator(valorX,nVariaveis)
mapaK = pd.DataFrame(matriz)#Aqui ta o mapa de Karnought.
#print(mapaK)
#print("Simplificação da equação lógica")
#print(valorX)
#Apartir do número de variáveis que temos do problema podemos preecher o mapa de karnaught
if nVariaveis == 3:
	reader.mapaK(reader,valorX,nVariaveis,1)
	eqsimplificada = reader.interpretador(reader,1)#ESta aqui é a equação simplificada.
	print(''.join(eqsimplificada))
if nVariaveis == 4:
	reader4.karnaught(valorX,nVariaveis,1)
	equisimplificada = reader4.printer()# Esta aqui é a equação simplificada.
	print(''.join(equisimplificada))

