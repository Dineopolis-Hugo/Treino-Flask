from flask import Flask
app = Flask(__name__,static_folder="Static")
#definindo a pasta de arquivos estáticos

@app.route("/")
def home():
    return "<h1>digite <i>Static/index.html</i> para acessar o arquivo estatico</h1>"

@app.route("/add" , methods = ["POST"])
def add():
    return "<h1>dados recebidos</h1>"


if __name__ == "__main__":
    app.run(debug = True)