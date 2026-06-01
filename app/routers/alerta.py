from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    mensaje: str

alertas_db = [
    Alerta(id=1, mensaje="Stock bajo para Camiseta (S)"),
    Alerta(id=2, mensaje="Stock bajo para Jeans (L)"),
]

@router.get("/alertas", response_model=List[Alerta])
def get_alertas():
    return alertas_db

@router.post("/alertas", response_model=Alerta)
def create_alerta(alerta: Alerta):
    alertas_db.append(alerta)
    return alerta

@router.get("/alertas/{alerta_id}", response_model=Alerta)
def get_alerta(alerta_id: int):
    alerta = next((a for a in alertas_db if a.id == alerta_id), None)
    if alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    return alerta

@router.put("/alertas/{alerta_id}", response_model=Alerta)
def update_alerta(alerta_id: int, updated_alerta: Alerta):
    for index, alerta in enumerate(alertas_db):
        if alerta.id == alerta_id:
            alertas_db[index] = updated_alerta
            return updated_alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.delete("/alertas/{alerta_id}", response_model=Alerta)
def delete_alerta(alerta_id: int):
    alerta = next((a for a in alertas_db if a.id == alerta_id), None)
    if alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    alertas_db.remove(alerta)
    return alerta
