from flask import Flask ,request
from json import dumps
#biblioteca para transformar string em json
app = Flask(__name__,static_folder="Static")
#definindo a pasta de arquivos estáticos

@app.route("/")
def home():
    return "<h1>digite <i>Static/index.html</i> para acessar o arquivo estatico</h1>"

@app.route("/add",methods = ["GET","POST"])
#adicionando o método para a rota /add
def add():
    if request.method == "POST":
        #request.method controla as requisições
        return dumps(request.form)
        #retornando resultado com biblioteca dumps
        #convertendo os dados recebidos para o formato json

        # retornando resultado sem biblioteca
        # { return "ok post result %s" % request.form["nome"] }
    return "ok get"
  


if __name__ == "__main__":
    app.run(debug = True)