from flask import Flask, json, request, jsonify, make_response
import ClienteService
import Cliente
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "APP de Cliente em Python"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

@app.route('/clientes', methods=['GET'])
def findALL():
    clientes = ClienteService.findAll()
    json_string = json.dumps([o.dump() for o in clientes])
    return json_string

@app.route('/clientes/<int:id>', methods=['GET'])
def findById(id):
    cliente = ClienteService.findById(id)
    if (cliente == ""):
        json_string = "Não existe Cliente cadastrado com esse ID", id
    else:
        json_string = json.dumps({'id': cliente.id,
                                 'nome': cliente.nome,
                                 'cpf': cliente.cpf,
                                 'salario': str(cliente.salario),
                                 'ativo': cliente.ativo})
    return json_string

@app.route('/clientes', methods=['POST'])
def salvar():
    cliente = Cliente.Cliente(0, request.json['nome'],
                              request.json['cpf'],
                              request.json['salario'],
                              bool(request.json['ativo']))
    newCliente = ClienteService.inserirCliente(cliente)
    json_string = json.dumps({'id': cliente.id,
                             'nome': cliente.nome,
                             'cpf': cliente.cpf,
                             'salario': str(cliente.salario),
                             'ativo': cliente.ativo})

    return json_string

@app.route('/clientes/<int:id>', methods=['DELETE'])
def deleteById(id):
    cliente = ClienteService.findById(id)
    if (cliente == ""):
        json_string = "Não existe Cliente cadastrado com esse ID", id
    else:
        cliente = ClienteService.deleteCliente(id)
        json_string = "Cliente Deletado com sucesso!"

    return json_string

@app.route('/clientes/<int:id>', methods=['PUT'])
def updateCliente(id):
    if (cliente == ""):
        json_string = "Não existe Cliente cadastrado com esse ID", id
    else:
        cliente = Cliente.Cliente(request.json['id'],
                                  request.json['nome'],
                                  request.json['cpf'],
                                  request.json['salario'],
                                  (request.json['ativo']))
        cliente.id = id
        clienteAtualizado = ClienteService.updateCliente(cliente)
        json_string = json.dumps({'id': clienteAtualizado.id,
                                 'nome': clienteAtualizado.nome,
                                 'cpf': clienteAtualizado.cpf,
                                 'salario': str(clienteAtualizado.salario),
                                 'ativo': clienteAtualizado.ativo})
    return json_string

app.run()