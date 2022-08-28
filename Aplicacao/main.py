from flask import Flask, redirect, render_template, request, url_for
from flask import session
from flask import flash
import dao
from datetime import datetime
import smtplib
import email.message


app = Flask(__name__)
app.secret_key = 'autorizado'
#Ter variavel do usuario logado para validar no banco de dados // e utilizar o username setado em usuarioLogado no projeto\\
usuarioLogado = ""
#Variavel para poder pesquisar determinado produto na tabela de Produto em Uso// PRECISA SER GLOBAL PARA NAO DAR ERRO \\
produto = ""


#Iniciando a aplicacao
@app.route("/")
def Iniciar():
    return render_template("index.html")


#Funcao para o login
@app.route("/login", methods=["POST", "GET"])
def Login():
    global usuarioLogado
    usuarioLogado = request.form["username"]
    username = request.form["username"]
    senha = request.form["senha"]
    if dao.Logar(username, senha):
        #session['administrator'] = request.form['username']
        return redirect(url_for('Home'))
    else:
        flash('Dados inválidos')
        return render_template("index.html")

#Funcao para abrir tela de recuperacao de senha
@app.route("/recuperarSenha")
def AbrirRecuperarSenha():
    return render_template("recuperarSenha.html")

#Funcao para enviar email de recuperação de usuario e senha
@app.route("/recuperarSenha", methods=['POST'])
def RecuperarSenha():
    emailP = request.form['email']
    if dao.RecuperarSenha(emailP):
        usuario = dao.RecuperarUsuario(emailP)
        senha = dao.RecuperarSenha(emailP)
        corpo_email = """
        <p>Bem vindo a recuperação de conta</p>
        <p>Aqui está o seu usuário:</p>
        """  + str(usuario[0]).strip('(,)') +  """<p>Aqui está a sua senha:</p>""" + str(senha[0]).strip('(,)')

        msg = email.message.Message()
        msg['Subject'] = "Recuperando sua senha do login"
        msg['From'] = "easyaccessenai@gmail.com"
        msg['To'] = emailP
        password = "osziyjquovefcgpt"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        #Login credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))       
    else:
        flash("E-mail não cadastrado")
    return AbrirRecuperarSenha()


#Funcao para abrir tela onde pode cadastrar novo usuario
@app.route("/cadastrarUsuario")
def AbrirCadastroUsuario():
    return render_template("cadastrarUsuario.html")

#Funçao para inserir novo usuario
@app.route("/cadastrarUsuario", methods=["POST"])
def CadastrarUsuario():
    username = request.form["username"]
    email = request.form["email"]
    senha = request.form["senha"]
    validarSenha = request.form["validarSenha"]
    if senha == validarSenha:
        dao.CadastrarUsuario(username, email, senha)
        return redirect(url_for('Iniciar'))
    else:
        flash('A senhas devem ser repetidas!')
        return AbrirCadastroUsuario()


#Funcao para abrir tela de home
@app.route('/home')
def Home():
    #if 'administrator' in session:
    return render_template("home.html", usuario=usuarioLogado)
    #return redirect(url_for('Iniciar'))


#Funcao onde retorna a tabela de todos produtos em uso
#Retorna tambem o request do botao para pesquisar nome de um produto na tabela
@app.route("/produto", methods=['GET', 'POST'])
def Produtos():
    global produto
    #if 'administrator' in session:
    lista_banco = dao.Produtos()
    if request.method == 'POST':
        produto = request.form["pesquisarProduto"]
        if produto != None:
            lista_banco = dao.PesquisarProduto(produto)
        return render_template("produto.html", lista=lista_banco)
    else:
        return render_template("produto.html", lista=lista_banco)
    #return redirect(url_for('Iniciar'))

#Funcao para exclusao no botao da tabela de produtos
@app.route('/produtoExclusao', methods=['POST'])
def Excluir():
    id_produto = request.form['id_excluir']
    if id_produto != None:
        dao.ExcluirProduto(id_produto)
        return redirect(url_for('Produtos'))
    return render_template('produto.html', lista=dao.Produtos())


#Funcao para abrir tela de cadastrar produto
@app.route("/cadastrarProduto")
def AbrirCadastroProduto():
    return render_template("cadastrarProduto.html", cadastrarProduto=dao.VerProdutos())


#Funcao para atualizar quantidade do produto caso exista
@app.route("/atualizarProduto", methods=['POST'])
def AtualizarProduto():
    nome_produto_select = request.form['nome_produto_select']
    atualizar_quantidade = request.form['atualizar_quantidade']
    dao.SomarQuantidadeProdutos(atualizar_quantidade, nome_produto_select)
    return AbrirCadastroProduto()


#Funcao para inserir um produto na tabela de produtos
@app.route("/cadastrarProduto", methods=['POST'])
def InserirProduto():
    nome_produto = request.form['nome_produto']
    quantidade = request.form['quantidade']
    localizacao = request.form['localizacao']     
    dao.InserirProduto(nome_produto, quantidade, localizacao)
    return AbrirCadastroProduto()

#Funcao para abrir emprestimos com a lista de emprestimos
@app.route("/emprestimo")  
def Emprestimo():
    #if 'administrator' in session:  
    return render_template("emprestimo.html", geral=dao.Produtos(), emprestimo=dao.Emprestimos())
    #return redirect(url_for('Iniciar'))

#Funcao para inserir um novo emprestimo na tabela
@app.route("/emprestimo", methods=['POST'])  
def InserirEmprestimo():
    nome_produto = request.form['nome_produto']
    quantidade = request.form['quantidade']
    solicitante = request.form['solicitante']
    responsavel = request.form['responsavel']
    hora_do_emprestimo = request.form['hora_do_emprestimo']
    dao.SubtrairQuantidadeProdutos(quantidade, nome_produto)
    dao.InserirEmprestimo(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo)
    return Emprestimo()

#Funcao para devolver o produto para almoxarife e atualizar quantidade disponivel
@app.route("/produtoDevolucao", methods=['POST'])
def DevolverProdutoRelatorio():
    nome_produto = request.form['nome_produto']
    quantidade = request.form['quantidade']
    solicitante = request.form['solicitante']
    responsavel = request.form['responsavel']
    hora_do_emprestimo = request.form['hora_do_emprestimo']
    hora_da_devolucao = datetime.now()
    dao.SomarQuantidadeProdutos(quantidade, nome_produto)
    dao.InserirRelatorio(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao)
    dao.DeletarEmprestimo(nome_produto)
    return Emprestimo()

#Funcao para carregar pagina de reservas de produtos
@app.route("/reserva", methods=['GET'])
def Reserva():
    #if 'administrator' in session:
    return render_template("reserva.html", reserva=dao.VerProdutos(), lista=dao.TabelaReservas())
    #return redirect(url_for('Iniciar'))

#Funcao para inserir uma reserva na tabela
@app.route("/reserva", methods=['POST'])
def ReservarProduto():
    nome_produto = request.form['reservar_select']
    solicitante = request.form['solicitante']
    quantidade = request.form['quantidade']
    hora_da_reserva = request.form['hora_da_reserva']
    dao.ReservarProduto(nome_produto, solicitante, quantidade, hora_da_reserva)
    return Reserva()

#Funcao para excluir reserva
@app.route("/reservaExclusao", methods=['POST'])
def ExcluirReserva():
    id_reserva = request.form['id_reserva']
    dao.ExcluirReserva(id_reserva)
    return Reserva()


#Funcao para carregar relatorios dos produtos na tabela
@app.route("/relatorio")
def Relatorio():
    #if 'administrator' in session:
    return render_template("relatorio.html", relatorio=dao.Relatorios())
    #return redirect(url_for('Iniciar'))

#Funcao para filtrar a busca em relatorio
@app.route("/filtroRelatorio", methods=['POST'])
def FiltroRelatorio():
    hora_do_emprestimo = request.form['hora_do_emprestimo']
    hora_da_devolucao = request.form['hora_da_devolucao']
    if hora_da_devolucao != None and hora_da_devolucao > hora_do_emprestimo:
        return render_template("relatorio.html", relatorio = dao.FiltroRelatorio(hora_do_emprestimo, hora_da_devolucao))            
    return Relatorio()
    
#Encerrando aplicacao e voltando para a tela de login
@app.route("/logout")
def Logout():
    #session.pop('administrator', None)
    return redirect(url_for('Iniciar'))


#Funcao para debugar sem precisar parar o projeto
app.run(debug=True)
