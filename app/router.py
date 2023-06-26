from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RecipeSchema, RequestRecipe, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/create')
async def create(request:RequestRecipe,db:Session=Depends(get_db)):
    crud.create_recipe(db, recipe=request.parameter)
    crud.get_recipe_by_id(db, recipe_id=request.parameter.id)
    _recipes = crud.get_recipe(db, 0, 100)
    return {
        "code": 200,
        "status": "ok",
        "message": "Recipe created successfully",
        "result": _recipes
    }

@router.get('/')
async def get(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)): 
    _recipes = crud.get_recipe(db, skip, limit)
    return {
        "code": 200,
        "status": "ok",
        "message": "Success Fetch all data",
        "result": _recipes
    }

@router.get('/{id}')
async def get_by_id(id:int, db:Session = Depends(get_db)): 
    _recipe = crud.get_recipe_by_id(db, recipe_id=id)
    return {
        "code": 200,
        "status": "ok",
        "message": "Success get data",
        "result": _recipe
    }

@router.patch('/{id}')
async def update_recipe(request: RequestRecipe, db:Session = Depends(get_db)): 
    _recipe = crud.update_recipe(db, recipe_id=request.parameter.id, name=request.parameter.name, ingredients=request.parameter.ingredients, duration=request.parameter.duration)
    return Response(code=200, status='ok', message='Success update data', result=_recipe)

@router.delete('/{id}')
async def get_by_id(id:int, db:Session = Depends(get_db)): 
    crud.remove_recipe(db, recipe_id=id)
    return Response(code=200, status='ok', message='Success delete data').dict(exclude_none=True)