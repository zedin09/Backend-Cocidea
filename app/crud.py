from sqlalchemy.orm import Session
from model import Recipe
from schemas import RecipeSchema
from typing import List

def get_recipe(db:Session,skip:int=0,limit:int=100):
    return db.query(Recipe).offset(skip).limit(limit).all()

def get_recipe_by_id(db:Session,recipe_id:int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def create_recipe(db:Session, recipe:RecipeSchema):
    _recipe = Recipe(name=recipe.name, ingredients=recipe.ingredients, duration=recipe.duration)
    db.add(_recipe)
    db.commit()
    db.refresh(_recipe)
    return _recipe

def update_recipe(db:Session,recipe_id:int,name:str,ingredients:List[str],duration:str):
    _recipe = get_recipe_by_id(db=db,recipe_id=recipe_id)
    _recipe.name = name
    _recipe.ingredients = ingredients
    _recipe.duration = duration
    db.commit()
    db.refresh(_recipe)
    return _recipe

def remove_recipe(db:Session, recipe_id:int):
    _recipe = get_recipe_by_id(db=db,recipe_id=recipe_id)
    db.delete(_recipe)
    db.commit()
