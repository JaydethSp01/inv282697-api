from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: float
    imagen: str

productos_db = [
    Producto(id=1, nombre="Camisa", categoria="Ropa", precio=29.99, imagen="/images/camisa.jpg"),
    Producto(id=2, nombre="Pantalón", categoria="Ropa", precio=39.99, imagen="/images/pantalon.jpg"),
]

@router.get("/productos", response_model=List[Producto])
async def get_productos():
    return productos_db

@router.get("/productos/{producto_id}", response_model=Producto)
async def get_producto(producto_id: int):
    for producto in productos_db:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.post("/productos", response_model=Producto)
async def create_producto(producto: Producto):
    productos_db.append(producto)
    return producto

@router.put("/productos/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, producto: Producto):
    for idx, p in enumerate(productos_db):
        if p.id == producto_id:
            productos_db[idx] = producto
            return producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.delete("/productos/{producto_id}")
async def delete_producto(producto_id: int):
    for idx, producto in enumerate(productos_db):
        if producto.id == producto_id:
            del productos_db[idx]
            return {"message": "Producto deleted"}
    raise HTTPException(status_code=404, detail="Producto not found")
