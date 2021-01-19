import json

class Cliente:
    id=0
    nome=""
    cpf=""
    salario=0
    ativo=True

    def __init__(self, id, nome, cpf, salario, ativo):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.ativo = ativo

    @classmethod
    def from_json(clscls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def dump(self):
        return {'id': self.id,
                 'nome': self.nome,
                 'cpf': self.cpf,
                 'salario': str(self.salario),
                 'ativo': self.ativo}
