from flask import Blueprint, request

from app.serializers.receitas_serializer import ReceitaSerializer
from app.services.receitas.receitas_manage_csv import listar_receitas, buscar_receitas, gravar_receita

bp = Blueprint('receitas_route', __name__)


@bp.route("/receitas")
def lista_receitas():
    receitas = listar_receitas()

    return {"data": ReceitaSerializer.from_collection(receitas)}


@bp.route("/receitas", methods=['POST'])
def cria_receitas():
    data = request.get_json()
    resultado = gravar_receita(data['nome_da_receita'], data['descricao_da_receita'])
    return {"data": resultado.get('data')}, resultado.get('status')


@bp.route('/receitas/<nome>')
def busca_receita(nome):
    return {"data": buscar_receitas(nome)}
