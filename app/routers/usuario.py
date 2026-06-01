from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

usuarios_db = [
    Usuario(id=1, nombre="Juan Perez", email="juan.perez@example.com"),
    Usuario(id=2, nombre="Maria Gomez", email="maria.gomez@example.com"),
]

@router.get("/usuarios", response_model=List[Usuario])
async def get_usuarios():
    return usuarios_db

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
async def get_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")

@router.post("/usuarios", response_model=Usuario)
async def create_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    return usuario

@router.put("/usuarios/{usuario_id}", response_model=Usuario)
async def update_usuario(usuario_id: int, usuario: Usuario):
    for idx, u in enumerate(usuarios_db):
        if u.id == usuario_id:
            usuarios_db[idx] = usuario
            return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")

@router.delete("/usuarios/{usuario_id}")
async def delete_usuario(usuario_id: int):
    for idx, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            del usuarios_db[idx]
            return {"message": "Usuario deleted"}
    raise HTTPException(status_code=404, detail="Usuario not found")
