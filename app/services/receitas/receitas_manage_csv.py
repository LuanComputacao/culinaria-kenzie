import csv

from environs import Env

env = Env()
env.read_env()


def listar_receitas():
    with open(env('RECEITAS_CSV')) as f:
        reader = csv.DictReader(f)
        return [receita for receita in reader]


def buscar_receitas(nome):
    with open(env('RECEITAS_CSV')) as f:
        reader = csv.DictReader(f)
        return [receita
                for receita in reader
                if receita['nome_da_receita'].lower().startswith(nome.lower())
                ]
