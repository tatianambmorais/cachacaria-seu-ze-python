from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app) 


def translate(conselhos):
    "Função para traduzir texto"
    try:
        # introduz a variável que guardará os objetos
        data = []
        for conselho in conselhos:
            #traduz o texto
            traduzido = GoogleTranslator(source='en', target='pt').translate(conselho['advice'])
            # passa o ID e o advice, de modo que siga o mesmo padrão do GET original da API, para não conflitar com o código principal
            conselhoObjetoTraduzido = {"id": conselho["id"], "advice": traduzido}
            data.append(conselhoObjetoTraduzido)
        return data
    except Exception as e:
        return f"Erro encontrado: {e}"


@app.route('/translate', methods=['POST'])
def translate_my_text():
    "Endpoint para traduzir o texto"
    dados = request.json
    texto = dados.get('texto')
    # caso o texto não seja passado
    if not texto:
        return jsonify({"erro": "Ocorreu um erro na análise do texto. Tente novamente mais tarde"})
    else:
        textos = translate(texto)
        return jsonify(textos)
        
    


def obter_conselho():
    """Função para buscar um conselho da API."""
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            data = response.json()
            return data['slip']
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
