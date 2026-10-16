from flask import Flask
app = Flask(__name__)

@app.route("/")
def idex():
    return "index"
#add rota por decorator


#add rota por função
def teste():
    return "<p>Teste</p>"
app.add_url_rule("/teste","teste",teste)
#no add.url_rule, o 1 parâmetro é a rota,
#o 2 é o nome da função,
#o 3 é a função que será executada

def teste2():
    return "<h1>Teste 2</h1>"
app.add_url_rule("/teste-2","teste-2",teste2)

#rota dinâmica
@app.route("/hello/")
#faz funcionar a rota sem variável, caso o usuário não passe o nome

@app.route("/hello/<nome>")
def hello(nome = ""):
    return "<h1>hello,{}</h1>".format(nome)
#adicionando variável na rota dinâmica e retornando na função

@app.route("/blog/")
@app.route("/blog/<int:postID>")
def blog(postID = None):
    if postID is not None:
        if postID <= 0:
            postID = None

    if postID is None:
            return "<h1>Blog todo</h1>"
    else:
            return "<h1>Blog post {}</h1>".format(postID)

@app.route("/blog2/")
@app.route("/blog2/<float:postID>")
def blog2(postID = None):
    if postID is not None:
        if postID <= 0:
            postID = None

    if postID is None:
            return "<h1>Blog todo.float</h1>"
    else:
            return "<h1>Blog post.float {}</h1>".format(postID)
    #versão float da rota dinâmica   


if __name__ == "__main__":
    app.run(debug = True, port = 3000)
#port muda a porta padrão 