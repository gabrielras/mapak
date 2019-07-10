class Kcounter:
	def contador(pos,matriz):
		count = int(0)
		for i in range(0,4):
			for j in range(0,4):
				if matriz[i][j]==2:
					count=count+1
		return count