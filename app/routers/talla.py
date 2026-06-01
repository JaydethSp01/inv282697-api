from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Talla(BaseModel):
    id: int
    nombre: str

tallas_db = [
    Talla(id=1, nombre="S"),
    Talla(id=2, nombre="M"),
    Talla(id=3, nombre="L"),
]

@router.get("/tallas", response_model=List[Talla])
async def get_tallas():
    return tallas_db

@router.get("/tallas/{talla_id}", response_model=Talla)
async def get_talla(talla_id: int):
    for talla in tallas_db:
        if talla.id == talla_id:
            return talla
    raise HTTPException(status_code=404, detail="Talla not found")

@router.post("/tallas", response_model=Talla)
async def create_talla(talla: Talla):
    tallas_db.append(talla)
    return talla

@router.put("/tallas/{talla_id}", response_model=Talla)
async def update_talla(talla_id: int, talla: Talla):
    for idx, t in enumerate(tallas_db):
        if t.id == talla_id:
            tallas_db[idx] = talla
            return talla
    raise HTTPException(status_code=404, detail="Talla not found")

@router.delete("/tallas/{talla_id}")
async def delete_talla(talla_id: int):
    for idx, talla in enumerate(tallas_db):
        if talla.id == talla_id:
            del tallas_db[idx]
            return {"message": "Talla deleted"}
    raise HTTPException(status_code=404, detail="Talla not found")
