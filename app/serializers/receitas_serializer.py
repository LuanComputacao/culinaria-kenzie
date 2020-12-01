from typing import List

from app.models.receitas_model import Receita


class ReceitaSerializer:
    @staticmethod
    def from_collection(receita_collection: List[Receita]):
        receitas_serializadas = []
        for receita in receita_collection:
            receitas_serializadas.append({
                "id": receita.get_id(),
                "nome": receita.get_nome(),
                "descricao": receita.get_descricao()
            })

        return receitas_serializadas
