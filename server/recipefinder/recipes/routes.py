from flask import Blueprint, jsonify, request, current_app
from recipefinder import db
from recipefinder.models import Recipe, RecipeSchema
from recipefinder.globalutils import token_required

recipes = Blueprint('recipes', __name__)

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)


@recipes.get('/recipes')
def get_all_recipes():
    page = request.args.get('page', 1, type=int)
    # print(page)
    recipes = Recipe.query.order_by(
        Recipe.created_at.desc()).paginate(per_page=1, page=page)
    result = recipes_schema.dump(recipes.items)
    return jsonify(result), 200


@recipes.post('/recipes')
@token_required
def create_recipes(current_user):
    data = request.json
    title = data['title']
    link = data['link']
    instruction = data['instruction']
    try:
        new_recipe = Recipe(title=title, link=link,
                            instruction=instruction, creator=current_user)
        db.session.add(new_recipe)
        db.session.commit()
    except:
        jsonify({'message': 'Error creating recipe'}), 400
    db.session.flush()
    return recipe_schema.jsonify(new_recipe)


@recipes.get('/recipes/<int:recipe_id>')
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'the recipe does not exist'}), 400
    return recipe_schema.jsonify(recipe)


@recipes.patch('/recipes/<int:recipe_id>')
@token_required
def edit_recipe(current_user, recipe_id):
    if not current_user:
        return jsonify({'message': 'must login'}), 400
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'the recipe does not exist'}), 404
    if current_user != recipe.creator:
        return jsonify({'message': 'You do not have permission to edit this post'}), 401
    data = request.json
    recipe.title = data['title']
    recipe.link = data['link']
    recipe.instruction = data['instruction']
    db.session.commit()
    return recipe_schema.jsonify(recipe)


@recipes.patch('/recipes/<int:recipe_id>/like')
@token_required
def like_recipe(current_user, recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'the recipe does not exist'}), 400
    recipe.update_like(current_user)
    db.session.commit()
    return recipe_schema.jsonify(recipe), 201


@recipes.patch('/recipes/<int:recipe_id>/dislike')
@token_required
def dislike_recipe(current_user, recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'the recipe does not exist'}), 400
    recipe.update_dislike(current_user)
    db.session.commit()
    return recipe_schema.jsonify(recipe), 201


@recipes.patch('/recipes/<int:recipe_id>/save')
@token_required
def save_recipe(current_user, recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'message': 'the recipe does not exist'}), 400
    recipe.update_saved(current_user)
    db.session.commit()
    return recipe_schema.jsonify(recipe), 201
