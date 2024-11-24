from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 

def obter_conselho():
    """Função para buscar um conselho da API."""
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            data = response.json()
            return data['slip']['advice']
        else:
            return "Não foi possível obter um conselho no momento. Tente novamente mais tarde."
    except Exception as e:
        return f"Erro ao acessar a API: {e}"

@app.route('/conselhos/<int:quantidade>', methods=['GET'])
def obter_conselhos(quantidade):
    """Endpoint para obter conselhos."""
    conselhos = []
    for i in range(quantidade):
        conselho = obter_conselho()
        conselhos.append(conselho)
    return jsonify(conselhos)


if __name__ == "__main__":
    app.run(debug=True)
