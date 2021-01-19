import Conexao
import Cliente

def inserir(cliente):
    conexao = Conexao.conexaoBanco()
    novoId = buscarIdAtual()
    #novoId = (if () () + 1)
    if (novoId == None):
        novoId = 1.0
    else:
        novoId = (novoId + 1)

    sql = "Insert into cliente(id, nome, cpf, salario, ativo) values (%s, %s, %s, %s, %s)"
    clienteSql = [int(novoId), cliente.nome, cliente.cpf, cliente.salario, (cliente.ativo == "True" and 1 or 0)]
    try:
        c=conexao.cursor()
        c.execute(sql, clienteSql)
        conexao.commit()
        print("Registro Inserido")
    except Exception as ex:
        print(ex)

    conexao.close()
    newCliente = findById(novoId)
    return newCliente

def buscarIdAtual():
    conexao = Conexao.conexaoBanco()
    try:
        sql = "Select max(id) from cliente"
        c=conexao.cursor()
        c.execute(sql)
        (total,) = c.fetchone()
        if total:
            print(total)
    except Exception as ex:
        print(ex)

    conexao.close()
    return total

def findById(id):
    conexao = Conexao.conexaoBanco()
    cliente = ""
    try:
        sql = "Select * from cliente where id = %s"
        c=conexao.cursor()
        c.execute(sql, params=[id])
        myCursor = c.fetchall()
        for row in myCursor:
            id = row[0]
            nome = row[1]
            cpf = row[2]
            salario = row[3]
            ativo = row[4]

            cliente = Cliente.Cliente(id, nome, cpf, salario, ativo)

    except Exception as ex:
        print(ex)

    conexao.close()
    return cliente

def findAll():
    conexao = Conexao.conexaoBanco()
    clientes = []
    try:
        sql = "Select * from cliente"
        c=conexao.cursor()
        c.execute(sql)
        myCursor = c.fetchall()
        for row in myCursor:
            id = row[0]
            nome = row[1]
            cpf = row[2]
            salario = row[3]
            ativo = row[4]

            cli = Cliente.Cliente(id, nome, cpf, salario, ativo)
            clientes.append(cli)

    except Exception as ex:
        print(ex)

    conexao.close()
    return clientes

def updateCliente(cliente):
    conexao = Conexao.conexaoBanco()
    sql = "Update cliente set nome = %s, cpf = %s, salario = %s, ativo = %s where id = %s"
    clienteSql = [cliente.nome, cliente.cpf, cliente.salario, (cliente.ativo == "True" and 1 or 0), cliente.id]
    try:
        c=conexao.cursor()
        c.execute(sql, clienteSql)
        conexao.commit()
    except Exception as ex:
        print(ex)

    conexao.close()
    clienteAtualizado = findById(cliente.id)
    return clienteAtualizado

def deleteCliente(id):
    conexao = Conexao.conexaoBanco()
    try:
        sql = "Delete from cliente where id = %s"
        c=conexao.cursor()
        c.execute(sql, params=[id])
        conexao.commit()
    except Exception as ex:
        print(ex)

    conexao.close()