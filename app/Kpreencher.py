class Kpreencher:
	def preencher(pos,vetor):
		i = int(0)
		for i in range(0,len(vetor)):
			if(vetor[i]==1):
				vetor[i]=2
		return vetor
			
	