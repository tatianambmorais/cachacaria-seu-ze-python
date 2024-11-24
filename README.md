Conselhos do Seu Zé
Este é um simples aplicativo Flask que consome a API https://api.adviceslip.com/advice para fornecer conselhos aleatórios. O aplicativo expõe um endpoint que retorna uma lista de conselhos com base na quantidade solicitada.

Tecnologias
Flask: Framework web para Python.
Flask-CORS: Extensão para permitir compartilhamento de recursos entre diferentes origens.
Requests: Biblioteca para fazer requisições HTTP.

Instalação
Clone este repositório ou baixe os arquivos para o seu computador.
Crie um ambiente virtual:
python -m venv venv
Ative o ambiente virtual:
Windows: venv\Scripts\activate
Linux/MacOS: source venv/bin/activate

Instale as dependências:

pip install flask flask-cors requests

Uso
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

Considerações
A API utilizada pode estar indisponível ou retornar falhas. Caso isso ocorra, o servidor responderá com uma mensagem de erro.
O CORS está habilitado, permitindo que o servidor seja acessado de qualquer origem.
#   c a c h a c a r i a - s e u - z e  
 