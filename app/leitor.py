#Inputs iniciais do usuario
	#print("Em relcao a quais variaveis voce deseja montar sua equacao logica?")
	#print("Digite-as na ordem desejada, utilizando uma letra ou algarismo por variavel")
	#variables = input()
	#numVar = len(variables)
class leitor:
	def EquationReader(pos,equation,nvar):
		#print("Quantas variaveis serao usadas em sua equacao logica?")
		numVar =nvar
		#print("Insira sua equacao logica expressa com as letras escolhidas:\n Exemplo: Se A representa 1,	A' representa 0") 
		equacaoString = equation


		#PreProcessing: Quais variaveis 
		variables = "+"
		i = 0
		specials = "()'+*"

		while i < len(equacaoString):
			if equacaoString[i] in variables:
				i+=1
			elif equacaoString[i] not in specials:
				variables = variables + equacaoString[i]
				i+=1
			else:
				i+=1

		#Checagem da quantidade e da ordem das variaveis na equacao
		if numVar > (len(variables)-1):
			print("A quantidade de variaveis relatada(",numVar,") nao coincide com o numero real de variaveis na equacao (",len(variables)-1,").")
			print("Deseja continuar mesmo assim?")
			decisao = input("S/N\n")

			if decisao == "N":
				import sys
				sys.exit("Reinicie o programa.")
			elif decisao == "S":
				print("O programa continuara com",numVar-1,"variaveis (",variables,").")	

		numVar = len(variables)-1
		#print("Deseja reordenar as variaveis? A ordem atual e",variables,".)")
		#decisao = input("S/N\n")
		'''
		if decisao == "S":
			while 1==1:
				variables2 = input("Qual e a ordem desejada?\n")
				i = 0
				while i < numVar:
					if variables[i] not in variables2:
						i = -1
						break;
					elif variables2[i] not in variables:
						i = -2
					i+=1

				if i == -1:
					print("Uma das variaveis da equacao esta ausente na nova ordem. Repita a operacao.")
				if i == -2:
					print("Uma das variaveis inseridas na nova ordem nao existe na equacao. Repita a operacao.")
				if i == numVar:
					variables = variables2
					print("A nova ordem e",variables,".")
					break;

		'''
		#Criando e setando a matriz das entradas na tabela-verdade
		import numpy as np
		
		entradasTabela = np.zeros((2**numVar,numVar+1))
		coluna = numVar - 1

		while coluna >= 0:
			linha = 0
			passo = 2**(numVar-1-coluna)
			contador = 0
			bit = 0

			while linha <= (2**numVar)-1:
				if contador == passo:
					if bit == 0:
						bit = 1
					elif bit == 1:
						bit = 0
					contador = 0

				entradasTabela[linha][coluna] = bit

				contador+=1
				linha+=1

			coluna-=1


		#Imprimindo a matriz da Tabela-Verdade com uma coluna extra S de sa�da

		#print(variables)
		#print(entradasTabela)

		#transformacao da equacao logica em equacao matematica
		i=0
		equacaoString = equacaoString + "+"
		equacaoMath = "+"
		while i<len(equacaoString)-1:
			if equacaoString[i] in specials:
		#if equacaoString[i]=="+" and i!=0:
		#	equacaoMath = equacaoMath + ")+("
		#elif equacaoString[i] =="+" and i==0:
		#	equacaoMath = equacaoMath + "+("
		#elif equacaoString[i] =="+" and i==0:
		#	equacaoMath = equacaoMath + ")+"
				if equacaoString[i]=="'" and equacaoString[i+1]=="(":
					equacaoMath = equacaoMath + equacaoString[i] + "*"
				elif equacaoString[i] == ")" and equacaoString[i+1] == "(":
					equacaoMath = equacaoMath + equacaoString[i] + "*"
				else:
					equacaoMath = equacaoMath + equacaoString[i]
			elif equacaoString[i] in variables:
				if equacaoString[i-1]==")" or equacaoString[i-1]=="'":
					equacaoMath = equacaoMath + "*"
				equacaoMath = equacaoMath + equacaoString[i]
				if equacaoString[i+1] in variables and equacaoString[i+1] != "+":
					equacaoMath = equacaoMath + "*"
				elif equacaoString[i+1] == "(" and equacaoString[i+1] != "+":
					equacaoMath = equacaoMath + "*"
			i+=1

		#substitui��es progressivas ao longo da tabela-verdade:
		m=0
		while m <=(2**numVar)-1:

			#cria correspondencia entre as posicoes da variavel de variables e o respectivo valor do bit de bitSet
			bitSet = "+"
			i = 0
			equacaoOp = equacaoMath
			while i < numVar:
				if entradasTabela[m][i] == 1:
					bitSet = bitSet + "1"
				elif entradasTabela[m][i] == 0:
					bitSet = bitSet + "0"
				i+=1

			#substitui todas as inst�ncias da variavel equacaoOp pelo respectivo valor de bitSet 
			i = 0
			while i < len(variables):
				equacaoOp = equacaoOp.replace(variables[i],bitSet[i])
				i+=1


			#loop de loops de operacoes de algebra booleana; se s�o realizados, eles se repetem mais uma vez (i==0 quebra o loop)
			i = 1
			while i == 1:
				i = 0
				#remove as barras que se cancelam
				while "''" in equacaoOp:
					equacaoOp = equacaoOp.replace("''","")
					i = 1

				#inverte os bits onde possivel
				while "1'" in equacaoOp or "0'" in equacaoOp:
					equacaoOp = equacaoOp.replace("1'","0")
					equacaoOp = equacaoOp.replace("0'","1")
					i = 1

				#multiplica os bits onde possivel
				while "1*1" in equacaoOp or "0*0" in equacaoOp or "1*0" in equacaoOp or "0*1" in equacaoOp:
					equacaoOp = equacaoOp.replace("1*1","1")
					equacaoOp = equacaoOp.replace("0*0","0")
					equacaoOp = equacaoOp.replace("1*0","0")
					equacaoOp = equacaoOp.replace("0*1","0")
					i = 1
				
				#soma os bits onde possivel -> FONTE DE ERRO: 1+1*(0+0) REALIZA 1+1 E 0+0 --> PRESO NESTE LOOP ABC=000
				verif = 1
				while "1+1" in equacaoOp or "0+0" in equacaoOp or "1+0" in equacaoOp or "0+1" in equacaoOp:
					while verif == 1:		
					
						equacaoOp = equacaoOp.replace("*1+1","UM")
						equacaoOp = equacaoOp.replace("*0+0","DOIS")
						equacaoOp = equacaoOp.replace("*1+0","TRES")
						equacaoOp = equacaoOp.replace("*0+1","QUATRO")
					
						equacaoOp = equacaoOp.replace("1+1*","CINCO")
						equacaoOp = equacaoOp.replace("0+0*","SEIS")
						equacaoOp = equacaoOp.replace("1+0*","SETE")
						equacaoOp = equacaoOp.replace("0+1*","OITO")

						verif = 0
						while "1+1" in equacaoOp or "0+0" in equacaoOp or "1+0" in equacaoOp or "0+1" in equacaoOp:
							equacaoOp = equacaoOp.replace("1+1","1")
							equacaoOp = equacaoOp.replace("0+0","0")
							equacaoOp = equacaoOp.replace("1+0","1")
							equacaoOp = equacaoOp.replace("0+1","1")
							verif = 1
				

						equacaoOp = equacaoOp.replace("UM","*1+1")
						equacaoOp = equacaoOp.replace("DOIS","*0+0")
						equacaoOp = equacaoOp.replace("TRES","*1+0")
						equacaoOp = equacaoOp.replace("QUATRO","*0+1")
					
						equacaoOp = equacaoOp.replace("CINCO","1+1*")
						equacaoOp = equacaoOp.replace("SEIS","0+0*")
						equacaoOp = equacaoOp.replace("SETE","1+0*")
						equacaoOp = equacaoOp.replace("OITO","0+1*")

						i = 1
					if verif == 0:
						break

				#remove os parenteses onde possivel
				while "(1)" in equacaoOp or "(0)" in equacaoOp:
					equacaoOp = equacaoOp.replace("(1)","1")
					equacaoOp = equacaoOp.replace("(0)","0")
					i = 1

			#proxima linha (proxima entrada)
			entradasTabela[m][numVar] = int(equacaoOp[1])
			
			#print(bitSet) #teste
			#print(equacaoOp[1])#teste
			m+=1
		return entradasTabela


		#testes:
		#print(equacaoMath)
		#print(entradasTabela)
