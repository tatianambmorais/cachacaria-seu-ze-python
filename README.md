# Conselhos do Seu Zé
Este é um simples aplicativo Flask que consome a API https://api.adviceslip.com/advice para fornecer conselhos aleatórios. O aplicativo expõe um endpoint que retorna uma lista de conselhos com base na quantidade solicitada.

# Tecnologias
Flask: Framework web para Python.
Flask-CORS: Extensão para permitir compartilhamento de recursos entre diferentes origens.
Requests: Biblioteca para fazer requisições HTTP.

## Como executar o frontend

1. Instale o [Node.js](https://nodejs.org/) se ainda não o tiver.
2. Instale o `http-server` globalmente com o seguinte comando:

   ```bash
   npm install -g http-server
   
3. Navegue até o diretório onde está o arquivo conselho.html.

4. Execute o servidor local com o comando:

bash
http-server -p 8080
Abra o navegador e acesse http://localhost:8080/index.html para visualizar a aplicação

# Instalação backend
Clone este repositório ou baixe os arquivos para o seu computador.

1. Crie um ambiente virtual:
python -m venv venv

2. Ative o ambiente virtual:
Windows: venv\Scripts\activate
Linux/MacOS: source venv/bin/activate

3. Instale as dependências:
pip install flask flask-cors requests
pip install deep-translator
4. Uso
Para iniciar o servidor Flask, execute o comando:
python api-seu-ze.py

Para obter conselhos, faça uma requisição GET para o endpoint /conselhos/<quantidade>, onde <quantidade> é o número de conselhos que você deseja. Por exemplo, para obter 3 conselhos, faça a requisição para:

bash
http://127.0.0.1:5000/conselhos/3

O retorno será um JSON com os conselhos, assim:
[
  "Conselho 1",
  "Conselho 2",
  "Conselho 3"
]

Exemplo de Requisição
Requisição:

GET http://127.0.0.1:5000/conselhos/5

Resposta:
[
  "Seja corajoso.",
  "A persistência é o caminho para o sucesso.",
  "Não tenha medo de recomeçar.",
  "Acredite em você mesmo.",
  "A paciência traz bons resultados."
]

# Considerações
A API utilizada pode estar indisponível ou retornar falhas. Caso isso ocorra, o servidor responderá com uma mensagem de erro.
O CORS está habilitado, permitindo que o servidor seja acessado de qualquer origem.
