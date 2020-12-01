import csv

from environs import Env

from app.models.receitas_model import Receita

env = Env()
env.read_env()

fieldnames = ['id', 'nome_da_receita', 'descricao_da_receita']


def listar_receitas():
    with open(env('RECEITAS_CSV')) as f:
        reader = csv.DictReader(f)
        return [
            Receita(
                receita['nome_da_receita'],
                receita['descricao_da_receita'],
                receita['id']
            )
            for receita in reader]


def buscar_receitas(nome):
    with open(env('RECEITAS_CSV')) as f:
        reader = csv.DictReader(f)
        return [receita
                for receita in reader
                if receita['nome_da_receita'].lower().startswith(nome.lower())
                ]


def pega_ultimo_id():
    receita = {'id': 1}
    with open(env('RECEITAS_CSV')) as f:
        for receita in csv.DictReader(f):
            pass

        return int(receita.get('id'))


def verifica_se_receita_existe(nome):
    with open(env('RECEITAS_CSV')) as f:
        receitas = [receita
                    for receita in csv.DictReader(f)
                    if receita.get('nome_da_receita') == nome]
        return len(receitas) > 0


def gravar_receita(nome, descricao):
    if verifica_se_receita_existe(nome):
        return {'status': 409, 'data': "Receita já existe"}

    novo_id = pega_ultimo_id() + 1

    receita = {
        'id': novo_id,
        'nome_da_receita': nome,
        'descricao_da_receita': descricao
    }
    with open(env('RECEITAS_CSV'), 'a+') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(receita)
        return {'status': 201, 'data': receita}
