class MatrixCreator:
	def matrixCreator(pos,nV):
		j = 0
		i = 0
		mat = []
		if nV == 3:
			n = 4
			m = 2
		if nV == 4:
			n = int(4)
			m = int(4)
		for i in range(0,m):
			mat.append( [] )
		for i in range(0,m):
			for j in range(0,n):
				mat[i].append(j)
				mat[i][j] = 0
		return mat
	