from flask import Blueprint,request,redirect,url_for,session


auth_bp = Blueprint("auth",__name__,template_folder="templates")


@auth_bp.route("/",methods =["GET","POST"])
def login():
    if request.method == "POST":
        #pegar dados do form

        user = request.form["user"]
        password = request.form["password"]

        session["user"] = user
        session["token"] = "token aleatorio"
        #Token pra checar se o user ta com session ativa

        #return redirect ("user/dashboard")
        return redirect(url_for("user.dashboard"))
    return '''
            <form method = "POST">
            Usuário: <input type = "text" name = user /> <br>
            Senha: <input type = "password" name = password /> <br>
            <input type = "submit" value= "entrar" />
            </form>'''