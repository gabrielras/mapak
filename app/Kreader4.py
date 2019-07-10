from KaranoughtAlgorithm import kcreator
class Kreader4:
	agrupamento4x4 = 2
	agrupamento4x2_horizontal =[]
	agrupamento4x2_vertical = []
	agrupamento4x1_horizontal =[]
	agrupamento4x1_vertical = []
	agrupamento2x2=[]
	agrupamento2x1_vertical=[]
	agrupamento2x1_horizontal=[]
	unico = []
	def karnaught(self,valores,size,binario):
		reader = kcreator.MapaK
		matriz = reader.MapaCreator(valores,size)
		print("mapaK")
		print(matriz)
		if binario ==1:
			binario_linha=0
		elif binario ==0:
			binario_linha=1
		#Agrupamento 4x4:
		agrupamento4_4= int(1)
		for i in range(0,4):
			for j in range(0,4):
				if matriz[i][j] == binario_linha:
					agrupamento4_4 = 0;
		if agrupamento4_4 !=0:
			self.agrupamento4x4 = binario
			return self.agrupamento4x4
		#Olha esse binário aqui é importante.
		#Agrupamento 4x2
		for i in range(0,4):
			achou = False
			binariolinhain = False
			for j in range(0,4):
				if matriz[i][j]==binario_linha or matriz[(i+1)%4][j]==binario_linha:
					binariolinhain=True
				if matriz[i][j]==binario or matriz[(i+1)%4][j]==binario:
					achou=True
			if achou==True and binariolinhain!=True: #grupo existe e nao tem só dont care
				matriz[i][:]=[2,2,2,2]
				matriz[(i+1)%4][:]=[2,2,2,2] #trocando os elementos agrupados por dont care
				self.agrupamento4x2_horizontal.append(i) #guarda a informacao sobre o grupo
				#print(self.agrupamento4x2_horizontal)
		for j in range(0,4):
			achou = False
			binariolinhain = False
			for i in range(0,4):
				if matriz[i][j]==binario_linha or matriz[i][(j+1)%4]==binario_linha:
					binariolinhain=True
				elif matriz[i][j]==binario or matriz[i][(j+1)%4]==binario:
					achou==True
			if achou==True and binariolinhain!=True: #grupo existe e nao tem só dont care
				matriz[:][j]=[2,2,2,2]
				matriz[:][(j+1)%4]=[2,2,2,2] #trocando os elementos agrupados por dont care
				self.agrupamento4x2_vertical.append(j) #guarda a informacao sobre o grupo
				#print(self.agrupamento4x2_vertical)
				#Fim do caso 4x2
				#Inicio do caso 4x1
		'''
		for i in range(0,4):
			achou = False
			binariolinhain = False
			for j in range(0,4):
				if matriz[i][j]==binario_linha:
					binariolinhain=True
				elif matriz[i][j]==binario:
					achou==True
			if achou==True and binariolinhain!=True: #grupo existe e nao tem só dont care
				matriz[i][:]=[2,2,2,2]#trocando os elementos agrupados por dont care
				self.agrupamento4x1_horizontal.append(i) #guarda a informacao sobre o grupo
				print("Entrei aqui")
				#print("Agrupamento horizontal",self.agrupamento4x1_horizontal)
		'''
		for i in range(0,4):
			achou = False
			for j in range(0,4):
				if matriz[i][j]==binario_linha:
					achou = True
			if achou ==False and matriz[i][:]!=[2,2,2,2]:
				matriz[i][:]=[2,2,2,2]
				self.agrupamento4x1_horizontal.append(i)
		
		for j in range(0,4):
			achou = False
			for i in range(0,4):
				if matriz[i][j]==binario_linha:
					achou = True
			if achou ==False and matriz[:][j]!=[2,2,2,2]:
				for i in range(0,4):
					matriz[i][j]=2
				self.agrupamento4x1_vertical.append(j)
		'''
		for j in range(0,4):
			achou = False
			binariolinhain = False
			for i in range(0,4):
				if matriz[i][j]==binario_linha:
					binariolinhain=True
				elif matriz[i][j]==binario:
					achou==True
			if achou==True and binariolinhain!=True: #grupo existe e nao tem só dont care
				matriz[:][j]=[2,2,2,2]#trocando os elementos agrupados por dont care
				self.agrupamento4x1_vertical.append(j) #guarda a informacao sobre o grupo
				#print(self.agrupamento4x1_vertical)
		'''
		#Fim do caso 4x1
		#Inicio do caso 2x2
		for i in range(0,4):
			for j in range(0,4):
				if matriz[i][j]!=binario_linha and matriz[(i+1)%4][j]!=binario_linha and matriz[i][(j+1)%4]!=binario_linha and matriz[(i+1)%4][(j+1)%4]!=binario_linha:
					if matriz[i][j]==binario or matriz[(i+1)%4][j]==binario or matriz[i][(j+1)%4]==binario or matriz[(i+1)%4][(j+1)%4]==binario: #grupo existe
					        matriz[i][j]=2
					        matriz[(i+1)%4][j]=2
					        matriz[i][(j+1)%4]=2
					        matriz[(i+1)%4][(j+1)%4]=2
					        self.agrupamento2x2.append((10*i+j))
		#Inicio agrupamento2x1 de binarios					
		for j in range(0,4):
                	for i in range (0,4):
                		if matriz[i][j]!=binario_linha and matriz[(i+1)%4][j]!=binario_linha:
                			if matriz[i][j]==binario or matriz[(i+1)%4][j]==binario:
        	        			matriz[i][j]=2
        		        		matriz[(i+1)%4][j]=2
        			        	self.agrupamento2x1_vertical.append(10*i+j)
        	
		for i in range(0,4):        	
			for j in range(0,4):	
				if matriz[i][j]!=binario_linha and matriz[i][(j+1)%4]!=binario_linha:
        	        		if matriz[i][j]==binario or matriz[i][(j+1)%4]==binario:
        	        			matriz[i][j]=2
        	        			matriz[i][(j+1)%4]=2;self.agrupamento2x1_horizontal.append(10*j+i)
		for i in range(0,4):
			for j in range(0,4):
				if matriz[i][j]==binario:
					matriz[i][j]=2
					self.unico.append(10*i+j)
	def printer(self):
		resposta = []
		if self.agrupamento4x4!=2:
			return self.agrupamento4x4
		for i in range(0,len(self.agrupamento4x2_horizontal)):
			if self.agrupamento4x2_horizontal[i]==0:
				#print("A'")
				resposta.append("A'");
				resposta.append("+")
			elif self.agrupamento4x2_horizontal[i]==1:
				#print("B")
				resposta.append("B")
				resposta.append("+")
			elif self.agrupamento4x2_horizontal[i]==2:
				#print("A")
				resposta.append("A")
				resposta.append("+")
			elif self.agrupamento4x2_horizontal[i]==3:
				#print("B'")
				resposta.append("B'")
				resposta.append("+")
		for i in range(0,len(self.agrupamento4x2_vertical)):
			if self.agrupamento4x2_vertical[i]==0:
				#print("C'")
				resposta.append("C'")
				resposta.append("+")
			elif self.agrupamento4x2_vertical[i]==1:
				#print("D")
				resposta.append("D")
				resposta.append("+")
			elif self.agrupamento4x2_vertical[i]==2:
				#print("C")
				resposta.append("C")
				resposta.append("+")
			elif self.agrupamento4x2_vertical[i]==3:
				#print("D'")
				resposta.append("D'")
				resposta.append("+")
		for i in range(0,len(self.agrupamento4x1_horizontal)):
			if self.agrupamento4x1_horizontal[i]==0:
				#print("A'B'")
				resposta.append("A'B'")
				resposta.append("+")
			elif self.agrupamento4x1_horizontal[i]==1:
				#print("A'B")
				resposta.append("A'B")
				resposta.append("+")
			elif self.agrupamento4x1_horizontal[i]==2:
				#print("AB")
				resposta.append("AB")
				resposta.append("+")
			elif self.agrupamento4x1_horizontal[i]==3:
				#print("AB'")
				resposta.append("AB'")
				resposta.append("+")
		for i in range(0,len(self.agrupamento4x1_vertical)):
			if self.agrupamento4x1_vertical[i]==0:
				#print("C'D'")
				resposta.append("C'D'")
				resposta.append("+")
			elif self.agrupamento4x1_vertical[i]==1:
				#print("C'D")
				resposta.append("C'D")
				resposta.append("+")
			elif self.agrupamento4x1_vertical[i]==2:
				#print("CD")
				resposta.append("CD")
				resposta.append("+")
			elif self.agrupamento4x1_vertical[i]==3:
				#print("CD'")
				resposta.append("CD'")
				resposta.append("+")
		for i in range(0,len(self.agrupamento2x2)):
			if self.agrupamento2x2[i]==0:
				#print("A'C'")
				resposta.append("A'C'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==1:
				#print("A'D")
				resposta.append("A'D")
				resposta.append("+")
			elif self.agrupamento2x2[i]==2:
				#print("A'C")
				resposta.append("A'C")
				resposta.append("+")
			elif self.agrupamento2x2[i]==3:
				#print("A'D'")
				resposta.append("A'D'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==10:
				#print("BC'")
				resposta.append("BC'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==11:
				#print("BD")
				resposta.append("BD")
				resposta.append("+")
			elif self.agrupamento2x2[i]==12:
				#print("BC")
				resposta.append("BC")
				resposta.append("+")
			elif self.agrupamento2x2[i]==13:
				#print("BD'")
				resposta.append("BD'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==20:
				#print("AC'")
				resposta.append("AC'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==21:
				#print("AD")
				resposta.append("AD")
				resposta.append("+")
			elif self.agrupamento2x2[i]==22:
				#print("AC")
				resposta.append("AC")
				resposta.append("+")
			elif self.agrupamento2x2[i]==23:
				#print("AD'")
				resposta.append("AD'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==30:
				#print("B'C'")
				resposta.append("B'C'")
				resposta.append("+")
			elif self.agrupamento2x2[i]==31:
				#print("B'D")
				resposta.append("B'D")
				resposta.append("+")
			elif self.agrupamento2x2[i]==32:
				#print("B'C")
				resposta.append("B'C")
				resposta.append("+")
			elif self.agrupamento2x2[i]==33:
				#print("B'D'")
				resposta.append("B'D'")
				resposta.append("+")
		for i in range(0,len(self.agrupamento2x1_vertical)):
			if self.agrupamento2x1_vertical[i] == 0:
				#print("A'C'D'")
				resposta.append("A'C'D'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 10:
				#print("BC'D'")
				resposta.append("BC'D'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 20:
				#print("AC'D'")
				resposta.append("AC'D'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 30:
				#print("B'C'D'")
				resposta.append("B'C'D'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 1:
				#print("A'C'D")
				resposta.append("A'C'D")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 11:
				#print("BC'D")
				resposta.append("BC'D")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 21:
				#print("AC'D")
				resposta.append("AC'D")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 31:
				#print("B'C'D")
				resposta.append("B'C'D")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 2:
				#print("A'CD")
				resposta.append("A'CD")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] ==12:
				#print("BCD")
				resposta.append("BCD")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 22:
				#print("ACD")
				resposta.append("ACD")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 32:
				#print("B'CD")
				resposta.append("B'CD")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 3:
				#print("A'CD'")
				resposta.append("A'CD'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 13:
				#print("BCD'")
				resposta.append("BCD'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 23:
				#print("ACD'")
				resposta.append("ACD'")
				resposta.append("+")
			elif self.agrupamento2x1_vertical[i] == 33:
				#print("B'CD'")
				resposta.append("B'CD'")
				resposta.append("+")
		for i in range(0,len(self.agrupamento2x1_horizontal)):
			if self.agrupamento2x1_horizontal[i] == 0:
				#print("A'B'C'")
				resposta.append("A'B'C'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 10:
				#print("A'B'D")
				resposta.append("A'B'D")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 20:
				#print("A'B'C")
				resposta.append("A'B'C")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 30:
				#print("A'B'D'")
				resposta.append("A'B'D'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 1:
				#print("A'BC'")
				resposta.append("A'BC'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 11:
				#print("A'BD")
				resposta.append("A'BD")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 21:
				#print("A'BC")
				resposta.append("A'BC")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 31:
				#print("A'BD'")
				resposta.append("A'BD'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 2:
				#print("ABC'")
				resposta.append("ABC'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] ==12:
				#print("ABD")
				resposta.append("ABD")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 22:
				#print("ABC")
				resposta.append("ABC")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 32:
				#print("ABD'")
				resposta.append("ABD'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 3:
				#print("AB'C'")
				resposta.append("AB'C'")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 13:
				#print("AB'D")
				resposta.append("AB'D")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 23:
				#print("AB'C")
				resposta.append("AB'C")
				resposta.append("+")
			elif self.agrupamento2x1_horizontal[i] == 33:
				#print("AB'D'")
				resposta.append("AB'D'")
				resposta.append("+")
		for i in range(0,len(self.unico)):
			if self.unico[i] == 0:
				#print("A'B'C'D'")
				resposta.append("A'B'C'D'")
				resposta.append("+")
			elif self.unico[i] == 10:
				#print("A'BC'D'")
				resposta.append("A'BC'D'")
				resposta.append("+")
			elif self.unico[i] == 20:
				#print("ABC'D'")
				resposta.append("ABC'D'")
				resposta.append("+")
			elif self.unico[i] == 30:
				#print("AB'C'D'")
				resposta.append("AB'C'D'")
				resposta.append("+")
			elif self.unico[i] == 1:
				#print("A'B'C'D")
				resposta.append("A'B'C'D")
				resposta.append("+")
			elif self.unico[i] == 11:
				#print("A'BC'D")
				resposta.append("A'BC'D")
				resposta.append("+")
			elif self.unico[i] == 21:
				#print("ABC'D")
				resposta.append("ABC'D")
				resposta.append("+")
			elif self.unico[i] == 31:
				#print("AB'C'D")
				resposta.append("AB'C'D")
				resposta.append("+")
			elif self.unico[i] == 2:
				print("A'B'CD")
				resposta.append("A'B'CD")
				resposta.append("+")
			elif self.unico[i] ==12:
				print("A'BCD")
				resposta.append("A'BCD")
				resposta.append("+")
			elif self.unico[i] == 22:
				print("ABCD")
				resposta.append("ABCD")
				resposta.append("+")
			elif self.unico[i] == 32:
				print("AB'CD")
				resposta.append("AB'CD")
				resposta.append("+")
			elif self.unico[i] == 3:
				print("A'B'CD'")
				resposta.append("A'B'CD'")
				resposta.append("+")
			elif self.unico[i] == 13:
				print("A'BCD'")
				resposta.append("A'BCD'")
				resposta.append("+")
			elif self.unico[i] == 23:
				print("ABCD'")
				resposta.append("ABCD'")
				resposta.append("+")
			elif self.unico[i] == 33:
				print("AB'CD'")
				resposta.append("AB'CD'")
				resposta.append("+")
		resposta.pop()
		del self.agrupamento4x2_horizontal[:]
		del self.agrupamento4x2_vertical[:]
		del self.agrupamento4x1_horizontal[:]
		del self.agrupamento4x1_vertical[:]
		del self.agrupamento2x2[:]
		del self.agrupamento2x1_vertical[:]
		del self.agrupamento2x1_horizontal[:]
		del self.unico[:]
		self.agrupamento4x4 =2
		return resposta


