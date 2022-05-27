from flask import Flask, render_template, request
import dao

app = Flask (__name__)

@app.route("/")
def Iniciar():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def Login():
    email = request.form["email"]
    senha = request.form["senha"]

    if email == "admin@admin" and senha == "Admin":
        print("fwfqwrf")
    return render_template("home.html")

@app.route("/observacao")
def Observacao():

    return render_template("observacao.html")

@app.route("/produtoEmUso")
def ProdutoEmUso():
    return render_template("produtoEmUso.html", lista = dao.Produto_em_uso())

@app.route("/relatorio")
def Relatorio():
    return render_template("relatorio.html", lista = dao.Relatorio())

@app.route("/reserva", methods=['GET'])
def Reserva():
    return render_template("reserva.html", lista = dao.ReservarProdutos())

@app.route('/excluirProduto', methods=['POST'])
def Excluir():
    id_produto = request.form['id_excluir']
    dao.excluirProduto(id_produto)
    return render_template('produtoEmUso.html', lista = dao.Produto_em_uso())


app.run(debug=True)