"""KarnaughtCreator.py = This program creates a mapK"""
__author___ ="Emmanuel Sampaio"
from MatrixCreator import MatrixCreator
creator=MatrixCreator()
class MapaK:
	def MapaCreator(valores,size):
		if size == 3:
			matrix = creator.matrixCreator(size)
			matrix[0][:] = valores[0:4]
			matrix[1][:] = valores[4:8]
			aux = matrix[0][3]
			matrix[0][3] = matrix[0][2]
			matrix[0][2] = aux
			aux = matrix[1][3]
			matrix[1][3] = matrix[1][2]
			matrix[1][2] = aux
		if size ==4:
			matrix = creator.matrixCreator(size)
			n = int(0)
			for i in range(0,4):
				matrix[i][:]=valores[n:n+4]
				n = int(n+4)
			for i in range(0,4):
				aux = matrix[i][3]
				matrix[i][3] = matrix[i][2]
				matrix[i][2] = aux
			for i in range(0,4):	
				aux = matrix[3][i]
				matrix[3][i] = matrix[2][i]
				matrix[2][i] = aux
		return matrix
		
	



	

		
	



	
