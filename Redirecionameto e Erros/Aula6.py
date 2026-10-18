from flask import Flask,request,abort,redirect,url_for

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        if request.form ["nome"] == "admin" and request.form["senha"] == "admin":
            return redirect (url_for("sucesso"),code=302)
        #200 sucess,mas não redireciona
        #302 redireciona
        else:
            abort(401)
            #não autorizado
        #se o nome e a senha for admin redireciona pra /sucesso

    else:
        abort(403)
        #forbidden/proibido
        #Abort vai exibir algum erro q vc define EX:404,405,303...   


@app.route("/sucesso")
def sucesso():
    return "sucesso"

if __name__ == "__main__":
    app.run(debug=True)