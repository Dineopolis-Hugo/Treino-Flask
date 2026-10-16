from flask import Flask ,redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin():
    return "<h1>ADMIN</h1>"

@app.route("/guest/<name>")
def guest(name):
    return "<p>Olá Guest <b>%s</b></p>" %name
#outra forma de substituir a Var no html

@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for("admin"))
    #se o nome for admin, redireciona para a rota admin
    else:
        return redirect(url_for("guest", name = name))
    #senão, redireciona para a rota guest, passando o nome como parâmetro

@app.route("/google")
def google():
    return redirect("https://google.com")    

if __name__ == "__main__":
    app.run(debug=True)