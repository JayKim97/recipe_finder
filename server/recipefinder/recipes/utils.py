from recipefinder import db
from recipefinder.models import Tag, Category, Ingredient
from flask import jsonify


def init_tags(tags_str):
    all_tags = tags_str.split(", ")
    for index, tag in enumerate(all_tags, start=0):
        tag = tag.lower()
        exist = Tag.query.filter_by(name=tag).first()
        if not exist:
            temp = Tag(name=tag)
            all_tags[index] = temp
            db.session.add(temp)
        else:
            all_tags[index] = exist
    db.session.commit()
    return all_tags


def init_Category(categories_str):
    current_cates = categories_str.split(", ")
    for index, cate in enumerate(current_cates, start=0):
        cate = cate.lower()
        exist = Category.query.filter_by(name=cate).first()
        if not exist:
            temp = Category(name=cate)
            current_cates[index] = temp
            db.session.add(temp)
        else:
            current_cates[index] = exist
    db.session.commit()
    return current_cates


def init_ingredient(ingredients_str):
    ingredients = ingredients_str.split(", ")
    for index, ing in enumerate(ingredients, start=0):
        ing = ing.lower()
        exist = Ingredient.query.filter_by(name=ing).first()
        if not exist:
            temp = Ingredient(name=ing)
            ingredients[index] = temp
            db.session.add(temp)
        else:
            ingredients[index] = exist
    db.session.commit()
    return ingredients


def exist_checker(type, to_check):
    to_check.lower()
    if type == "tag":
        model = Tag
    elif type == "category":
        model = Category
    else:
        model = Ingredient
    return True if model.query.filter_by(name=to_check).first() else False


def recipe_jsonify(recipe):
    return {
        "created_at": recipe.created_at,
        "creator_name": recipe.creator.name,
        "creator_id": recipe.creator.id,
        "instruction": recipe.instruction,
        "id": recipe.id,
        "num_dislike": recipe.num_dislike,
        "num_likes": recipe.num_likes,
        "title": recipe.title,
        "link": recipe.link}
    # "tags": recipe.tags_string.split(", "),
    # "ingredients": recipe.ings_string.split(", "),
    # "categories": recipe.category_string.split(", ")}
