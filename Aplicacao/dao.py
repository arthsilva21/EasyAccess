import mysql.connector
#import pymysql

#1 - Usar no wamps
#2 - Usar no cloud
def conecta():
    #1
    #return pymysql.connect(user="root", password="@Dmin", host="localhost", database="dboAlmoxarife")
    #2
    #return mysql.connector.connect(host="localhost", user="root", password="@Dmin", database="dboAlmoxarife")
    return mysql.connector.connect(host="34.122.178.27", 
                                   user="root",
                                   password="@Dmin",
                                   database="dboAlmoxarife")

#Select no banco 'table usuarios' para logar no sistema
def Logar(usuario, senha):
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from usuarios where usuario = %s and senha = %s"
    valores = (usuario, senha)
    cursor.execute(sql, valores)
    return cursor.fetchall()

#Insert na tabela usuarios para cadastrar novo login do sistema
def CadastrarUsuario(usuario, email, senha):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into usuarios(usuario, email, senha) values (%s, %s, %s)"
    values = (usuario, email, senha)
    cursor.execute(sql, values)
    bd.commit()
    return "Usuario inserido com sucesso"

#Select na tabela usuarios para obter dados e enviar usuario para email cadastrado para recuperaçao
def RecuperarUsuario(email):
    bd = conecta()
    cursor = bd.cursor()
    sql = "select usuario from usuarios where email like %s"
    values = (email,)
    cursor.execute(sql, values)
    return cursor.fetchall()

#Select na tabela usuarios para obter dados e enviar senha para email cadastrado para recuperaçao
def RecuperarSenha(email):
    bd = conecta()
    cursor = bd.cursor()
    sql = "select senha from usuarios where email like %s"
    values = (email,)
    cursor.execute(sql, values)
    return cursor.fetchall()


#Select na tabela produtos para carregar todos os produtos
def Produtos():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from produtos order by id_produto desc"
    cursor.execute(sql)
    return cursor.fetchall()

#Select na tabela produto para ter apenas o produto desejado
def PesquisarProduto(nome):
    bd = conecta()
    cursor = bd.cursor()
    filtro = f'{nome}%'
    sql = "select * from produtos where nome_produto like %s"
    valores = (filtro,)
    cursor.execute(sql, valores)
    return cursor.fetchall()

#Delete em produto na tabela de produtos
def ExcluirProduto(id):
    bd = conecta()
    cursor = bd.cursor()
    sql = "delete from produtos where id_produto = %s"
    valor = (id,)
    cursor.execute(sql, valor)
    bd.commit()
    return 'Deletado'

#Insert na tabela produtos para inserir dados na tabela de produtos
def InserirProduto(nome_produto, quantidade, localizacao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into produtos(nome_produto, quantidade, localizacao) values (%s, %s, %s)"
    valores = (nome_produto, quantidade, localizacao)
    cursor.execute(sql, valores)
    bd.commit()
    return "inserido"


#Select apenas nome do produto na tabela de produtos para carregar no select de atualizar
def VerProdutos():
    bd = conecta()
    cursor = bd.cursor()
    ss = "select nome_produto from produtos"
    cursor.execute(ss)
    return cursor.fetchall()

#Select em toda tabela de emprestimos
def Emprestimos():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from emprestimos"
    cursor.execute(sql)
    return cursor.fetchall()

#Insert para inserir um novo emprestimo quando realizado
def InserirEmprestimo(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into emprestimos(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo) values (%s,%s,%s,%s,%s)"
    values = (nome_produto, quantidade, solicitante,
              responsavel, hora_do_emprestimo)
    cursor.execute(sql, values)
    bd.commit()

#Delete na tabela de emprestimo
def DeletarEmprestimo(nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    sql = "delete from emprestimos where nome_produto = %s"
    values = (nome_produto,)
    cursor.execute(sql, values)
    bd.commit()

#Select de toda tabela de reserva
def TabelaReservas():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from reservas order by id_reserva desc"
    cursor.execute(sql)
    return cursor.fetchall()

#Insert na tabela reservas
def ReservarProduto(nome_produto, solicitante, quantidade, hora_da_reserva):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into reservas(nome_produto, solicitante, quantidade, hora_da_reserva) values (%s, %s, %s, %s)"
    valor = (nome_produto, solicitante, quantidade, hora_da_reserva)
    cursor.execute(sql, valor)
    bd.commit()

#Delete na tabela de reserva
def ExcluirReserva(id_reserva):
    bd = conecta()
    cursor = bd.cursor()
    sql = "delete from reservas where id_reserva = %s"
    valor = (id_reserva,)
    cursor.execute(sql, valor)
    bd.commit()

#Select na tabela de relatorios
def Relatorios():
    bd = conecta()
    cursor= bd.cursor()
    sql = "select nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao from relatorios order by id_relatorio desc"
    cursor.execute(sql)
    return cursor.fetchall()

#Insert para inserir novo dado em relatorio quando excluir de emprestimo
def InserirRelatorio(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into relatorios(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao) values (%s,%s,%s,%s,%s,%s)"
    values = (nome_produto, quantidade, solicitante,
              responsavel, hora_do_emprestimo,hora_da_devolucao)
    cursor.execute(sql, values)
    bd.commit()

#Select para filtrar as datas dos relatorios
def FiltroRelatorio(hora_do_emprestimo, hora_da_devolucao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "select nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao from relatorios where hora_do_emprestimo between %s and %s"
    values = (hora_do_emprestimo, hora_da_devolucao)
    cursor.execute(sql, values)
    return cursor.fetchall()

#Update na tabela produtos para quando for realizado o emprestimo diminuir a quantidade emprestada na quantidade disponivel
#Update na tabela produtos para quando for realizado a exclusao de determinada quantidade de produto.
def SubtrairQuantidadeProdutos(quantidade, nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    sql = "update produtos set quantidade = quantidade - %s where nome_produto like %s"
    values = (quantidade, nome_produto)
    cursor.execute(sql, values) 
    bd.commit()


#Update na tabela produtos para quando chegar novos produtos e quando voltar de emprestimo
def SomarQuantidadeProdutos(quantidade, nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    sql = "update produtos set quantidade = quantidade + %s where nome_produto like %s"
    values = (quantidade, nome_produto)
    cursor.execute(sql, values) 

    bd.commit()