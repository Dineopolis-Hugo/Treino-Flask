from flask import Flask, render_template
#importando flask
#Render template para renderizar o html,css,Js

app = Flask(__name__)
#iniciando flask

#criar 1a página do site

#decorator: serve pra atribuir uma função a uma rota (sempre será declarada acima da função)
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#Rota dinâmica:
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html",nome_usuario = nome_usuario)
    #Passando o nome do usuário para o html, para que ele seja exibido na página

#rodar o site
if __name__ == "__main__":
#roda o que ta dentro do if se o arquivo for executado diretamente, e não importado    
    app.run(debug=True)
#Debug faz aparecer as altereções feitas no código sem precisar reiniciar o servidor