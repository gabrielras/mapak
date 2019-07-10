import random;
class BotGeradorDeTabela:
	def createTabelaVerdade(self,size):
		vetor = []
		choices = [1,0]
		for i in range(0,size):
			vetor.append(random.choice(choices))
		return vetor
	def choicecreator(self):
		choices = [3,4]
		numdevariaveis = random.choice(choices)
		return numdevariaveis