from colorama import Cursor
import mysql.connector


def conecta():
    return mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="@Rth1598",
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
def cadastrarUsuario(usuario, senha):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into usuarios(usuario, senha) values (%s, %s)"
    values = (usuario, senha)
    cursor.execute(sql, values)
    bd.commit()
    return "Usuario inserido com sucesso"


#Select na tabela produtos para carregar todos os produtos
def Produtos():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from produtos order by id desc"
    cursor.execute(sql)
    return cursor.fetchall()

#Insert na tabela produtos para inserir dados na tabela de produtos
def inserirProduto(nome_produto, quantidade, localizacao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into produtos(nome_produto, quantidade, localizacao) values (%s, %s, %s)"
    valores = (nome_produto, quantidade, localizacao)
    cursor.execute(sql, valores)
    bd.commit()
    return "inserido"


#EM USO
def PesquisarProduto(nome):
    bd = conecta()
    cursor = bd.cursor()
    filtro = f'{nome}%'
    sql = "select * from produtos where nome_produto like %s"
    valores = (filtro,)
    cursor.execute(sql, valores)
    return cursor.fetchall()


#EM USO


def excluirProduto(id):
    bd = conecta()
    cursor = bd.cursor()
    sql = "delete from produtos where id = %s"
    valor = (id,)
    cursor.execute(sql, valor)
    bd.commit()
    return 'Deletado'


def atualizarEstoque(quantidade, nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    quantidade_atual = buscaQuantidade(nome_produto)
    if quantidade_atual >= int(quantidade):
        total = int(quantidade_atual) - int(quantidade)
        sql = "update produtos set quantidade = %s where nome_produto = %s"
        valores = (total, nome_produto)
        cursor.execute(sql, valores)
        bd.commit()
    else:
        return 'Quantidade invalida!'


def adicionarEstoque(quantidade, nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    quantidade_atual = buscaQuantidade(nome_produto)
    if quantidade_atual >= int(quantidade):
        total = int(quantidade_atual) + int(quantidade)
        sql = "update produtos set quantidade = %s where nome_produto = %s"
        valores = (total, nome_produto)
        cursor.execute(sql, valores)
        bd.commit()


def buscaQuantidade(nome):
    bd = conecta()
    cursor = bd.cursor()
    ss = "select quantidade from produtos where nome_produto like %s"
    valor = (nome,)
    cursor.execute(ss, valor)
    quanti = cursor.fetchone()
    return int(quanti[0])

#EM USO


def VerProdutos():
    bd = conecta()
    cursor = bd.cursor()
    ss = "select nome_produto from produtos"
    cursor.execute(ss)
    return cursor.fetchall()


def Emprestimos():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from emprestimos"
    cursor.execute(sql)
    return cursor.fetchall()

def InserirEmprestimo(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into emprestimos(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo) values (%s,%s,%s,%s,%s)"
    values = (nome_produto, quantidade, solicitante,
              responsavel, hora_do_emprestimo)
    cursor.execute(sql, values)
    bd.commit()


def DeletarEmprestimo(nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    sql = "delete from emprestimos where nome_produto = %s"
    values = (nome_produto,)
    cursor.execute(sql, values)
    bd.commit()




def ReservarProduto(nome_produto, solicitante, quantidade, hora_da_reserva):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into reservas(nome_produto, solicitante, quantidade, hora_da_reserva) values (%s, %s, %s, %s)"
    valor = (nome_produto, solicitante, quantidade, hora_da_reserva)
    cursor.execute(sql, valor)
    bd.commit()


def TabelaReservas():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from reservas order by id_reserva desc"
    cursor.execute(sql)
    return cursor.fetchall()

def ExcluirReserva(id_reserva):
    bd = conecta()
    cursor = bd.cursor()
    sql = "delete from reservas where id_reserva = %s"
    valor = (id_reserva,)
    cursor.execute(sql, valor)
    bd.commit()

def Relatorios():
    bd = conecta()
    cursor= bd.cursor()
    sql = "select nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao from relatorios order by id_relatorio desc"
    cursor.execute(sql)
    return cursor.fetchall()

def InserirRelatorio(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into relatorios(nome_produto, quantidade, solicitante, responsavel, hora_do_emprestimo, hora_da_devolucao) values (%s,%s,%s,%s,%s,%s)"
    values = (nome_produto, quantidade, solicitante,
              responsavel, hora_do_emprestimo,hora_da_devolucao)
    cursor.execute(sql, values)
    bd.commit()

def FiltroRelatorio(hora_do_emprestimo, hora_da_devolucao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from relatorios where hora_do_emprestimo between %s and %s"
    values = (hora_do_emprestimo, hora_da_devolucao)
    cursor.execute(sql, values)
    return cursor.fetchall()

def SubtrairQuantidadeProdutos(quantidade, nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    sql = "update produtos set quantidade = quantidade - %s where nome_produto like %s"
    values = (quantidade, nome_produto)
    cursor.execute(sql, values) 
    bd.commit()

def SomarQuantidadeProdutos(quantidade, nome_produto):
    bd = conecta()
    cursor = bd.cursor()
    sql = "update produtos set quantidade = quantidade + %s where nome_produto like %s"
    values = (quantidade, nome_produto)
    cursor.execute(sql, values) 
    bd.commit()