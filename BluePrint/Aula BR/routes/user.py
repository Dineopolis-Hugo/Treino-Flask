from flask import Blueprint,render_template,session,redirect,url_for


user_bp = Blueprint("user",__name__,template_folder="templates")
#passa o nome da rota e name pra identificar que é uma partição




@user_bp.route("/")
def root():
    return '''
            <h1>Bem vindo à página do usuário!</h1>
            '''
# 3 apostrofos pra ficar multilinha

@user_bp.route("/settings")
def settings():
    return "Configurações do usuário"

@user_bp.route("/dashboard")
def dashboard():
    name = session.get("user")
    return render_template("dashboard.html",name = name)

@user_bp.before_request
#Executa uma função antes de qualquer requisição que passe pelo Blueprint
def check_autentication():
    #validação de section
    if "token" not in session:
        return redirect(url_for("auth.login"))
        #no urlfor passa o NOME da função da rota
