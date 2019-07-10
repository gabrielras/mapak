'''
__author__ = "Emmanuel Sampaio,Carlos Alfredo"
__maintainer__ = "Emmanuel Sampaio"
__email__ = "emmanuelsampaio@alu.ufc.br"
__status__ = "testing moment".
'''
from KaranoughtAlgorithm import kcreator
class kreader8:
	linha_de_uns = []
	quadrado_de_uns = []
	dupla_de_uns = []
	coluna_de_uns = []
	unico= []
	todomundo = '2'
	def mapaK(self,valores,size,binario):
		self.todomundo = '2'
		reader = kcreator.MapaK
		matriz = reader.MapaCreator(valores,size)
		#Vamos criar o método para ler as 4 variáveis.
		nbinarioinverso = 0
		test = True
		for i in range(0,len(valores)):
			if valores[i]!=0:
				test=False
		if(test==True):
			self.todomundo='0'
			return self.todomundo
		if binario == 0 :
			binario_inverso =1
		else:
			binario_inverso =0
		for i in range(0,4):
			if valores[i]==binario_inverso:
				nbinarioinverso = nbinarioinverso + 1	
		achou =False
		for i in range(0,2):
			for j in range(0,4):
				if matriz[i][j]==binario_inverso:
					achou = True
		if achou == False:
			self.todomundo = '1'
			return self.todomundo
		#Condição de linhas de binário
		for i in range(0,2):
			achou = False
			for j in range(0,4):
				if matriz[i][j]==binario_inverso:
					achou = True
			if achou ==False:
				matriz[i][:]=[2,2,2,2]
				self.linha_de_uns.append(i)
		numberof2 = self.check2(matriz)
		if nbinarioinverso + numberof2==8:
			return "programa findo"#Olha esse return 
		#Condição dos quadrados de 1
		#print(matriz)
		for i in range(0,2):
			for j in range(0,4):
				achou_binario = False
				achou = False
				if matriz[i][j] == binario or matriz[i][(j+1)%4]==binario or matriz[(i+1)%2][j] == binario or matriz[(i+1)%2][(j+1)%4]==binario:
					achou_binario = True
				if  matriz[i][j] == binario_inverso or matriz[i][(j+1)%4]==binario_inverso or matriz[(i+1)%2][j] == binario_inverso or matriz[(i+1)%2][(j+1)%4]==binario_inverso:
					achou = True
				if achou == False and achou_binario == True:
					matriz[i][j]=2
					matriz[i][(j+1)%4] = 2
					matriz[(i+1)%2][j] = 2
					matriz[(i+1)%2][(j+1)%4] = 2
					self.quadrado_de_uns.append(10*i+j)
		#print(matriz)
		numberof2 = self.check2(matriz)
		if nbinarioinverso + numberof2==8:
			return "programa findo"
		#Condição das duplas de 1.
		for i in range(0,2):
			for j in range(0,4):
				achou_binario=False
				if  matriz[i][j]!=binario_inverso and matriz[i][((j+1)%4)]!=binario_inverso:
					if matriz[i][j]==binario or matriz[i][(j+1)%4]==binario:
						achou_binario=True
				if  achou_binario == True:
					matriz[i][j]=2
					matriz[i][(j+1)%4] =2
					self.dupla_de_uns.append(i*10+j)
		numberof2 = self.check2(matriz)
		#print(matriz)
		if (nbinarioinverso + numberof2)==8:
			return "programa findo"
		#Condição das colunas de 1
		for j in range(0,4):
			achou_binario = False
			if matriz[0][j]!=binario_inverso and matriz[1][j]!=binario_inverso:
				if matriz[0][j]==binario or matriz[1][j]==binario:
					achou_binario =True
			if achou_binario ==True:
				matriz[0][j] = 2  
				matriz[1][j] = 2
				self.coluna_de_uns.append(j)
		numberof2 = self.check2(matriz)
		#print(matriz)
		if (nbinarioinverso + numberof2)==8:
			return "programa findo"
		for i in range(0,2):
			for j in range(0,4):
				if matriz[i][j]==binario:
					self.unico.append(10*i+j)
					matriz[i][j]=2
	def check2(matriz):
		counter2 = int(0)
		for i in range(0,2):
			for j in range(0,4):
				if matriz[i][j]==2:
					counter2 = counter2+1
		return counter2
	def interpretador(self,binario):
		simplificada = []
		if self.todomundo !='2':
			return self.todomundo
		for i in range(0,len(self.linha_de_uns)):
			if self.linha_de_uns[i]==1:
				if binario==0:
					#print("A'")
					simplificada.append("A'")
					simplificada.append("+")	
				else:
					#print("A")
					simplificada.append("A")
					simplificada.append("+")
					
			else:
				if binario ==0:
					#print("A")
					simplificada.append("A")
					simplificada.append("+")

				else:
					#print("A'")
					simplificada.append("A'")
					simplificada.append("+")
		for i in range(0,len(self.quadrado_de_uns)):
			if self.quadrado_de_uns[i]==0:
				#print("B'")
				simplificada.append("B'")
				simplificada.append("+")
			elif self.quadrado_de_uns[i]==1:
				#print("C")
				simplificada.append("C")
				simplificada.append("+")
			elif self.quadrado_de_uns[i]==2:
				#print("B")
				simplificada.append("B")
				simplificada.append("+")
			elif self.quadrado_de_uns[i]==3:
				#print("C'")
				simplificada.append("C'")
				simplificada.append("+")
		for i in range(0,len(self.dupla_de_uns)):
			if self.dupla_de_uns[i]==0:
				#print("A'B'")
				simplificada.append("A'B'")
				simplificada.append("+")
			elif self.dupla_de_uns[i]==1:
				#print("A'C")
				simplificada.append("A'C")
				simplificada.append("+")
			elif self.dupla_de_uns[i]==2:
				#print("A'B")
				simplificada.append("A'B")
				simplificada.append("+")
			elif self.dupla_de_uns[i]==3:
				#print("A'C'")
				simplificada.append("A'C'")
				simplificada.append("+")
			if self.dupla_de_uns[i]==10:
				#print("AB'")
				simplificada.append("AB'")
				simplificada.append("+")
			elif self.dupla_de_uns[i]==11:
				#print("AC")
				simplificada.append("AC")
				simplificada.append("+")
			elif self.dupla_de_uns[i]==12:
				#print("AB")
				simplificada.append("AB")
				simplificada.append("+")
			elif self.dupla_de_uns[i]==13:
				#print("AC'")
				simplificada.append("AC'")
				simplificada.append("+")
		for i in range(0,len(self.coluna_de_uns)):
			if self.coluna_de_uns[i]==0:
				#print("B'C'")
				simplificada.append("B'C'")
				simplificada.append("+")
			elif self.coluna_de_uns[i]==1:
				#print("B'C")
				simplificada.append("B'C")
				simplificada.append("+")
			elif self.coluna_de_uns[i]==2:
				#print("BC")
				simplificada.append("BC")
				simplificada.append("+")
			elif self.coluna_de_uns[i]==3:
				#print("BC'")
				simplificada.append("BC'")
				simplificada.append("+")
		for i in range(0,len(self.unico)):
			if self.unico[i]==0:
				#print("A'B'C'")
				simplificada.append("A'B'C'")
				simplificada.append("+")
			elif self.unico[i]==1:
				#print("A'B'C")
				simplificada.append("A'B'C")
				simplificada.append("+")
			elif self.unico[i]==2:
				#print("A'BC")
				simplificada.append("A'BC")
				simplificada.append("+")
			elif self.unico[i]==3:
				#print("A'BC'")
				simplificada.append("A'BC'")
				simplificada.append("+")
			if self.unico[i]==10:
				#print("AB'C'")
				simplificada.append("AB'C'")
				simplificada.append("+")
			elif self.unico[i]==11:
				#print("AB'C")
				simplificada.append("AB'C")
				simplificada.append("+")
			elif self.unico[i]==12:
				#print("ABC")
				simplificada.append("ABC")
				simplificada.append("+")
			elif self.unico[i]==13:
				#print("ABC'")
				simplificada.append("ABC'")
				simplificada.append("+")
		simplificada.pop()
		del self.linha_de_uns[:] 
		del self.quadrado_de_uns[:]
		del self.dupla_de_uns[:]
		del self.coluna_de_uns[:]
		del self.unico[:]
		self.todomundo = '2'
		return simplificada


