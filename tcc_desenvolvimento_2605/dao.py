import mysql.connector


def conecta():
    return mysql.connector.connect( host="localhost",
                                    user="root",
                                    password="admin",
                                    database="dboAlmoxarife")


def inserirProduto(nome_produto, quantidade, localizacao):
    bd = conecta()
    cursor = bd.cursor()
    sql = "insert into produtos(nome_produto, quantidade, localizacao) values (%s, %s, %s)"
    valores = (nome_produto, quantidade,localizacao)
    cursor.execute(sql, valores)
    bd.commit()
    return "inserido"

#EM USO
def Produto_em_uso():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from produtos"
    cursor.execute(sql)
    
    return cursor.fetchall()

def excluirProduto(id):
    bd = conecta()
    cursor = bd.cursor()
    sql = 'delete from produtos where id = %s'
    valor = (id,)
    cursor.execute(sql, valor)
    bd.commit()
    return 'Deletado'
    

def atualizarEstoque(quantidade,nome_produto):
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

def adicionarEstoque(quantidade,nome_produto):
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
def ReservarProdutos():
    bd = conecta()
    cursor = bd.cursor()
    ss = "select nome_produto from produtos"
    cursor.execute(ss)
    return cursor.fetchall()
     
#EM USO
def Relatorio():
    bd = conecta()
    cursor = bd.cursor()
    sql = "select * from emprestimos"
    cursor.execute(sql)    
    return cursor.fetchall()