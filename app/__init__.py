from flask import Flask
from .routes.recipe import recipe_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(recipe_blueprint, url_prefix='/recipe')
    return app
