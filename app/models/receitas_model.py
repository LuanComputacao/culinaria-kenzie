from typing import List


class Ingrediente:
    def __init__(self, nome):
        self.nome = nome


class Receita:
    def __init__(self, nome, descricao, id=None):
        self._nome = nome
        self._descricao = descricao
        self._id = id
        self._ingredientes = []

    def add_ingredientes(self, ingredientes: List[Ingrediente]):
        ingredientes_com_repeticao = self._ingredientes + ingredientes
        self._ingredientes = list(set(ingredientes_com_repeticao))

    def add_ingrediente(self, ingrediente: Ingrediente):
        self._ingredientes.append(ingrediente)

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_id(self):
        return self._id


class ReceitaQuente():
    opcoes_de_aquecimento = ['forno', 'chama']
    identificacao = 'quente'

    def __init__(self, tipo_de_aquecimento: int):
        self.tipo_de_aquecimento = ReceitaQuente.opcoes_de_aquecimento[tipo_de_aquecimento]

    @classmethod
    def receita_de_forno(cls):
        return cls(0)

    @classmethod
    def receita_de_chama(cls):
        return cls(1)

    @staticmethod
    def get_recipiente(sigla: str):
        return 'panela' if sigla == 'p' else 'forma'
