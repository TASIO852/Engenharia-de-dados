import pandas as pd 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return "api ok"

@app.route("/dados")
def dados():
    tabela = pd.read_csv('C:/Users/tasio.guimaraes/Documents/Financas/Python/Analises/Data/centro_de_custo.csv')
    return jsonify(tabela)

app.run(host='0.0.0.0')