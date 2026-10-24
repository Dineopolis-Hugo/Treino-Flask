from tempfile import template

from flask import Flask,render_template,request

app = Flask(__name__,template_folder="template")


@app.route("/")
def notas():
    return render_template("notas.html")

@app.route("/calculo", methods=["POST"])
def calculo(): 
    qtd_notas=4
    total =sum([int(v) for v in request.form.to_dict().values()]) 
    # pega os valores trazidos do form,transforma cada valor do dict em int e dps soma todos eles

    media = total//qtd_notas
    return render_template ("calculo.html",media=media)
    #retornando a média para o template anmalisar se ta aprovado ou n

if __name__ == "__main__":
    app.run(debug=True)