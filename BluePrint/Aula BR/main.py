from flask import Flask
from routes.user import user_bp
#importando blueprint da outra pasta
from routes.Auth import auth_bp

app = Flask(__name__)
app.secret_key = "12345678"
#Toda vez que usar section precisa de secret key (armazenar no .env)

@app.route("/")
def root():
    return "<h1>Página inicial</h1>"



#registrando blueprint e adicionando prefixo rota
app.register_blueprint(user_bp, url_prefix = '/user')

app.register_blueprint(auth_bp,url_prefix = "/auth")

if __name__ == "__main__":
    app.run(debug=True,port=5153)
