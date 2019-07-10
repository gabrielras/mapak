'''''
Atualização dia 18/04/2019 By Emmanuel Sampaio:
O que o programa já consegue fazer:
1-Cria o mapa de Karnaught para 3 ou 4 variáveis(Usando Kcreator.py)
2-Consegue simplificar algumas situações para 3 variáveis
O que o programa NÃO consegue fazer:
1-Falta interpretar quando não tem linha de 1 
Atualização dia 19/04/2018 by Emmanuel Sampaio:
O que o atualizamos:
A capacidade do programa simplificar equações com trés variáveis foi expandida faltando apenas casos com don't care
O programa ainda NÃO consegue fazer:
Entender don't care
Entender mais de 3 variáveis.
'''''
from KaranoughtAlgorithm import kcreator
class Kreader:
	def karnaught(self,valores,size):
		reader = kcreator.MapaK
		i = int(0)
		count =int(0)
		posicao = 0
		while i<len(valores):
			if(valores[i]==1):
				count=count+1
			i=i+1
		numeroDeUns = count
		matriz = reader.MapaCreator(valores,size)#Recebe o Mapa de Karnaught
		#print(matriz)
		while numeroDeUns > 0:
			if size == 3: #Para mapas de 3 variáveis
				i = int(0)
				achou = False
				#Esse While verifica se uma linha só tem 1.
				linhade1 = False
				while achou == False and i < 4: 
					if matriz[0][i] != 1:
						achou = True
					i = int(i+1)
				if achou == False and numeroDeUns!=0:
					numeroDeUns = int(numeroDeUns - 4)
					linhade1 = True
					posicao = 1					
					print("A' ",end="")
				achou = False
				i = 0
				while achou == False and i<4:
					if matriz[1][i] !=1:
						achou = True
					i = int(i+1)
				if achou == False and numeroDeUns!=0:
					print("A ",end="")
					linhade1 = True
					posicao = 0
					numeroDeUns = int(numeroDeUns - 4)
				if numeroDeUns == 1 and linhade1==True:
					numeroDeUns = 0
					for i in range(0,4):
							if(matriz[1][i]==1 and matriz[0][i]==1):
								if i==0:
									print("+C'B'")
								elif i==1:
									print("+CB'")
								elif i==2:
									print("+CB")
								else:
									print("+C'B")
				#Se tivermos 1 linha de 1 e 2 variáveis sobrando.
				elif numeroDeUns == 2 and linhade1==True :
					
					for i in range(0,4):
						if(i<3 and matriz[1][i]==1 and matriz[1][i+1]==1 and matriz[0][i]==1 and matriz[0][i+1]==1):
							if i == 0:
								print("+B'")
								numeroDeUns = 0
							if i == 1:
								print("+C")
								numeroDeUns = 0
							if i == 2:
								print("+B")
								numeroDeUns = 0
						if(i==3 and matriz[1][i]==1 and matriz[0][i]==1 and matriz[0][0]==1 and matriz[1][0]==1):
							print("+C'")
							numeroDeUns = 0
						if(numeroDeUns!=0 and i<3 and matriz[posicao][i]==1 and matriz[posicao][i+1]!=1):
							if i == 0:
								print("+C'B'",end="")
								print("+CB")
								numeroDeUns = int(0)
							if i == 1:
								print("+B'C",end="")
								print("+BC'")
								numeroDeUns = int(0)
					
				elif numeroDeUns == 3 and linhade1==True:
					numeroDeUns = 0
					for i in range(0,4):
						if(matriz[posicao][i]==0):
							if(i==0):
								print("+B",end="")
								print("C")
							elif i==1:
								print("+B",end="")
								print("+C'")
							elif i==2:
								print("+B'",end="")
								print("+C'",end="")
							elif i==3:
								print("+B",end="")
								print("+C")
				if linhade1==False:
					quadrado = 0 #Número de Quadrados
					for i in range(0,4):
						if(i<3 and matriz[1][i]==1 and matriz[1][i+1]==1 and matriz[0][i]==1 and matriz[0][i+1]==1):
							if(i==0):
								print(" B'",end="")
								quadrado = quadrado+1
								numeroDeUns=numeroDeUns-4
							elif(i==1):
								print(" C",end="")
								if(quadrado==1):
									numeroDeUns = numeroDeUns-2
								else:
									quadrado = quadrado+1
									numeroDeUns = numeroDeUns-4
							elif(i==2):
								print(" B",end="")
								if quadrado==1:
									numeroDeUns = numeroDeUns-2
								else:
									quadrado = quadrado+1
									numeroDeUns = numeroDeUns-4
						if(i==3 and matriz[1][i]==1 and matriz[0][i]==1 and matriz[0][0]==1 and matriz[1][0]==1):
							print(" C'")
							if(quadrado==1):
								numerDeUns = numeroDeUns-2
							else:
								quadrado = quadrado+1
								numeroDeUns = numeroDeUns-4
					if(quadrado<=1 and numeroDeUns!=0):
						valor=int(0)
						duplas = 0#Verifica quantas duplas tem na linha 0
						duplas2 = 0#Verifica quantas duplas tem na linha1
						while valor<4:
							if(valor<3 and matriz[0][valor]==1 and matriz[0][valor+1]==1 ):
								if valor==0:
									duplas = duplas+1
									print(" A'B' ")
									numeroDeUns=numeroDeUns-2
								if valor==1:
									print(" A'C ")
									if(duplas>=1):
										numeroDeUns=numeroDeUns-1
									else:
										numeroDeUns= numeroDeUns-2
										duplas =duplas+1
								if valor==2:
									print(" A'B ")
									if(duplas>=1):
										numeroDeUns=numeroDeUns-1
									else:
										numeroDeUns= numeroDeUns-2
										duplas =duplas+1
							if(valor==3 and matriz[0][valor]==1 and matriz[0][0]==1 and (matriz[1][valor]!=1 or matriz[1][0]!=1)):
								print("A'C'")
								if(duplas>=1):
									numeroDeUns=numeroDeUns-1
								else:
									numeroDeUns= numeroDeUns-2
									duplas =duplas+1
							if(valor<3 and matriz[1][valor]==1 and matriz[1][valor+1]==1 ):
								if valor==0:
									print("AB'")
									duplas2 = duplas2+1
									numeroDeUns=numeroDeUns-2
								elif valor==1:
									print("AC")
									if duplas2>=1:
										numeroDeUns = numeroDeUns -2
									else:
										duplas = duplas2+1
										numeroDeUns = numeroDeUns-2
								elif valor==2:
									print("AB")
									if duplas2>=1:
										numeroDeUns = numeroDeUns -2
									else:
										duplas2 = duplas2+1
										numeroDeUns = numeroDeUns-2
							if(valor==3 and matriz[1][valor]==1 and matriz[1][0]==1 and (matriz[0][valor]!=1 or matriz[0][0]!=1)):
								print("AC'")
								if(duplas2>=1):
									numeroDeUns=numeroDeUns-1
								else:
									numeroDeUns= numeroDeUns-2
									duplas2 =duplas2+1
							valor=valor+1
						for i in range(0,4):
							if(numeroDeUns!=0 and i<3 and matriz[0][i]==1 and matriz[1][i]==1 and matriz[0][i+1]!=1 ):
								if(i==0 and matriz[0][3]!=1):
									print("B'C'")
									if matriz[1][1]==1 or matriz[1][3]==1:
										numeroDeUns = numeroDeUns-1
									else:
										numeroDeUns = numeroDeUns-2  
								elif i==1 and matriz[0][0]!=1:
									print("B'C")
									if matriz[1][2]==1 or matriz[1][0]==1:
										numeroDeUns = numeroDeUns - 1
									else:
										numeroDeUns = numeroDeUns -2
								elif i==2 and matriz[0][1]!=1:
									print("BC")
									if matriz[1][3]==1 or matriz[1][1]==1:
										numeroDeUns = numeroDeUns-1
									else:
										numeroDeUns = numeroDeUns-2
								if(numeroDeUns!=0 and i==3 and matriz[0][i]==1 and matriz[1][i]==1 and matriz[0][0]!=1 and matriz[0][2]!=1):
									print("BC'")
									if(matriz[1][2]==1 or matriz[1][0]==1):
										numeroDeUns = numeroDeUns-1
									else:
										numeroDeUns = numeroDeUns-2
						for i in range(0,4):	
								if(numeroDeUns!=0 and i<3 and matriz[1][i]==1 and matriz[0][i]==1 and matriz[1][i+1]!=1 ):
									if i==0 and matriz[1][3]!=1:
										print("B'C'")
										if matriz[0][1]==1 or matriz[0][3]==1:
											numeroDeUns = numeroDeUns-1
										else:
											numeroDeUns = numeroDeUns-2  
									elif i == 1 and matriz[1][0] != 1:
										print("B'C")
										if matriz[0][2]==1 or matriz[0][0]==1:
											numeroDeUns = numeroDeUns - 1
										else:
											numeroDeUns = numeroDeUns -2
									elif i == 2 and matriz[1][1] != 1:
										print("BC")
										if matriz[0][3]==1 or matriz[0][1]==1:
											numeroDeUns = numeroDeUns - 1
										else: 
											numeroDeUns = numeroDeUns - 2
									if(numeroDeUns!=0 and i==3 and matriz[1][i]==1 and matriz[0][i]==1 and matriz[1][0]!=1 and matriz[1][2]!=1):
										print("BC'")
										if(matriz[0][2]==1 or matriz[0][0]==1):
											numeroDeUns = numeroDeUns-1
										else:
											numeroDeUns = numeroDeUns-2
										 		
						for i in range(0,4):
							if numeroDeUns!=0 and i!=0 and i!=3 and matriz[0][i]==1 and matriz[0][i+1]!=1 and matriz[1][i]!=1:
								if i == 1:
									print("A'B'C")
									if numeroDeUns == 1:
										numeroDeUns = 0
									else:
										numeroDeUns = numeroDeUns -1
								elif i == 2:
									print("A'B C")
									
									if numeroDeUns ==1:
										numeroDeUns=0
									else:
										numeroDeUns = numeroDeUns -1
							if numeroDeUns != 0 and i!=0 and i!=3 and matriz[1][i] == 1 and matriz[1][i+1] != 1 and matriz[0][i] != 1:
								if i==1:
									print("AB'C")
									if numeroDeUns==1:
										numeroDeUns=0
									else: 
										numeroDeUns = numeroDeUns -1
								elif i==2:
									print("ABC")
									if numeroDeUns==1:
										numeroDeUns=0
									else: 
										numeroDeUns = numeroDeUns -1
							if numeroDeUns!=0 and i==0 and matriz[1][i]==1 and matriz[1][i+1]!=1 and matriz[0][0]!=1 and matriz[1][3]!=1:
								print("AB'C'")
								if numeroDeUns == 1:
									numeroDeUns = 0
								else: 
									numeroDeUns = numeroDeUns -1
							if numeroDeUns !=0 and i==0 and matriz[0][i]==1 and matriz[0][i+1]!=1 and matriz[0][3]!=1:								
								print("A'B'C'")
								if numeroDeUns==1:
									numeroDeUns=0
								else: 
									numeroDeUns = numeroDeUns -1
							if numeroDeUns!=0 and i==3 and matriz[1][i]==1 and matriz[1][i-1]!=1  and matriz[1][0]!=1:
								print("ABC'")
								if numeroDeUns==1:
									numeroDeUns = 0
								else: 
									numeroDeUns = numeroDeUns -1
							if numeroDeUns!=0 and i==3 and matriz[0][i]==1 and matriz[0][i-1]!=1 and matriz[0][0]!=1 and matriz[0][0]!=1:								
								print("A'BC'")
								if numeroDeUns==1:
									numeroDeUns=0
								else: 
									numeroDeUns = numeroDeUns -1
							


				


