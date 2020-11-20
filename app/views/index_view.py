from flask import Blueprint

bp = Blueprint('index_route', __name__)


@bp.route('/')
def index():
    return {"status": "Ok!"}
