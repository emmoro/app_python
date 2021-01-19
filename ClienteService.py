import Cliente
import ClienteDao

def inserirCliente(cliente):
    newCliente = ClienteDao.inserir(cliente)
    return newCliente

def findAll():
    clientes = ClienteDao.findAll()
    return clientes

def findById(id):
    cliente = ClienteDao.findById(id)
    return cliente

def buscarIdAtual():
    idAtual = ClienteDao.buscarIdAtual()

def deleteCliente(id):
    ClienteDao.deleteCliente(id)

def updateCliente(cliente):
    cliente = ClienteDao.updateCliente(cliente)
    return cliente