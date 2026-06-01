from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Categoria(BaseModel):
    id: int
    nombre: str

categorias_db = [
    Categoria(id=1, nombre="Ropa"),
    Categoria(id=2, nombre="Accesorios"),
]

@router.get("/categorias", response_model=List[Categoria])
async def get_categorias():
    return categorias_db

@router.get("/categorias/{categoria_id}", response_model=Categoria)
async def get_categoria(categoria_id: int):
    for categoria in categorias_db:
        if categoria.id == categoria_id:
            return categoria
    raise HTTPException(status_code=404, detail="Categoria not found")

@router.post("/categorias", response_model=Categoria)
async def create_categoria(categoria: Categoria):
    categorias_db.append(categoria)
    return categoria

@router.put("/categorias/{categoria_id}", response_model=Categoria)
async def update_categoria(categoria_id: int, categoria: Categoria):
    for idx, c in enumerate(categorias_db):
        if c.id == categoria_id:
            categorias_db[idx] = categoria
            return categoria
    raise HTTPException(status_code=404, detail="Categoria not found")

@router.delete("/categorias/{categoria_id}")
async def delete_categoria(categoria_id: int):
    for idx, categoria in enumerate(categorias_db):
        if categoria.id == categoria_id:
            del categorias_db[idx]
            return {"message": "Categoria deleted"}
    raise HTTPException(status_code=404, detail="Categoria not found")
