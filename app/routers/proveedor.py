from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Proveedor(BaseModel):
    id: int
    nombre: str
    contacto: str

proveedores_db = [
    Proveedor(id=1, nombre="Proveedor A", contacto="contacto@proveedora.com"),
    Proveedor(id=2, nombre="Proveedor B", contacto="contacto@proveedorb.com"),
]

@router.get("/proveedores", response_model=List[Proveedor])
async def get_proveedores():
    return proveedores_db

@router.get("/proveedores/{proveedor_id}", response_model=Proveedor)
async def get_proveedor(proveedor_id: int):
    for proveedor in proveedores_db:
        if proveedor.id == proveedor_id:
            return proveedor
    raise HTTPException(status_code=404, detail="Proveedor not found")

@router.post("/proveedores", response_model=Proveedor)
async def create_proveedor(proveedor: Proveedor):
    proveedores_db.append(proveedor)
    return proveedor

@router.put("/proveedores/{proveedor_id}", response_model=Proveedor)
async def update_proveedor(proveedor_id: int, proveedor: Proveedor):
    for idx, p in enumerate(proveedores_db):
        if p.id == proveedor_id:
            proveedores_db[idx] = proveedor
            return proveedor
    raise HTTPException(status_code=404, detail="Proveedor not found")

@router.delete("/proveedores/{proveedor_id}")
async def delete_proveedor(proveedor_id: int):
    for idx, proveedor in enumerate(proveedores_db):
        if proveedor.id == proveedor_id:
            del proveedores_db[idx]
            return {"message": "Proveedor deleted"}
    raise HTTPException(status_code=404, detail="Proveedor not found")
