from flask import Flask,request
import json
app= Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    # os 2 métodos abaixo retornam o argumento da URL, mas um é nativo
    # do python [T2] e o outro é da biblioteca flask [T1]
    t1 = request.args.to_dict()
    t2 = dict(request.args)


    #print(request.method,request.args)
    #métodos pra ler tipo de requisição e argumentos
    return json.dumps([t1["idade"],t2["nome"]])
#quando eu coloco esse parâmetro ele retorna se isso estiver declarado na url

#retornando resultado com biblioteca dumps

if __name__ =="__main__":
    app.run(debug=True)