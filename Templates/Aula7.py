from flask import Flask,render_template,request


app = Flask(__name__,template_folder="templates")

@app.route("/")
def index():
    x = 10
    y = 50
    query = request.args.to_dict()
    #Acessa argumentos/parâmetros enviados na URL e transforma em um dicionário (dict)

    return render_template("modelo.html",x=x, y=y, query=query)

if __name__ == ("__main__"):

    app.run(debug=True )