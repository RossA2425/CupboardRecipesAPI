from flask import Blueprint

recipe_blueprint = Blueprint('recipe', __name__)

@recipe_blueprint.route('/search_recipe', methods=['GET'])
def search_recipe():
    # Recipe search logic
    return "Recipe search results"
