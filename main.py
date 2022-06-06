from flask import Flask, render_template
from flask import request, redirect
import this
import pessoa
this.resultado = ""
market = Flask(__name__)

@market.route("/index", methods=['POST','GET'])
def homepage():
    return render_template("index.html", tituloIndex="HomePage")

@market.route("/index/cadastrar", methods=['POST','GET'])
def cad():
    if request.method == 'POST':
        name = request.form['nome']
        telephone = request.form['tel']
        address = request.form['end']
        date = request.form['dat']
        pessoa.cadastrar(name, telephone, address, date)
        return redirect('/index/consultar')
    elif request.method == 'GET':
        this.resultado = 51
    return render_template("cadastrar.html", tituloCadastro="Cadastrar Usuário")

@market.route("/index/consultar", methods=['POST','GET'])
def con():
    this.resultado = pessoa.consultar()
    return render_template("consultar.html", tituloConsultar="Consultar Usuário", resultado=this.resultado)

@market.route("/index/atualizar", methods=['POST','GET'])
def atu():
    return render_template("atualizar.html", tituloAtualizar="Atualizar Usuário")

@market.route("/index/excluir", methods=['POST','GET'])
def exc():
    return render_template("excluir.html", tituloExcluir="Excluir Usuário")

if __name__ == "__main__":
    market.run(debug=True)