from flask import Flask

from app.views.index_view import bp as index_bp
from app.views.receitas_view import bp as receitas_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index_bp)
    app.register_blueprint(receitas_bp)

    return app
