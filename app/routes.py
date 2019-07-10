from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import json
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

app = Flask(__name__)
  
@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	nVariaveis = int(request.form['email'])
	equation = request.form['name']

	entradasTabela = equationreader3.leitordaequacao(nVariaveis,equation)
	tabelaverdade = pd.DataFrame(entradasTabela)
	valorX = tabelaverdade.iloc[:][nVariaveis].values
	print(tabelaverdade)

	reader2 = kcreator.MapaK
	matriz = reader2.MapaCreator(valorX,nVariaveis)
	mapaK = pd.DataFrame(matriz)#Aqui ta o mapa de Karnought.
	print(mapaK)
	vetor1 = tabelaverdade.values.tolist()
	vetor = mapaK.values.tolist()
	teste1 = json.dumps(vetor1)
	teste = json.dumps(vetor)
	print(teste)
	
	return jsonify({ 'name' : teste , 'email' : teste1 })


if __name__ == '__main__':
	app.run(debug=True)