from flask import Flask,render_template,request,make_response

app = Flask(__name__,template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/setcookie",methods =["GET","POST"] )
def setcookie():

    resp = make_response(render_template("setcookie.html"))
#permite modificar a resposta HTTP, adicionando cookies e cabeçalhos antes de enviá-la ao navegador.
     
    if request.method == "POST":
        dados = request.form["c"]
        resp.set_cookie("testecookie",dados)
        #param 1: nome do cookie 
        #param 2: conteúdo do cookie    
    return resp


@app.route("/getcookie")
def getcookie():
    cookiename = request.cookies.get("testecookie")
    #puxando o cookie pra var (passando o nome como parâmetro)
    return f"<h1>o valor do cookie é: {cookiename}</h1>"


if __name__ == "__main__":
    app.run(debug=True)