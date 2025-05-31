from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.usuarios import UsuarioCreate, UsuarioOut
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.api.v1.crud.crud_usuario import crear_usuario_crud, listar_usuarios_crud, obtener_usuario_crud, actualizar_usuario_crud, eliminar_usuario_crud

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioOut)
def crear_usuario(usuarios: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario_crud(usuarios, db)

@router.get("/", response_model=List[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return listar_usuarios_crud(db)

@router.get("/{id}", response_model=UsuarioOut)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    return obtener_usuario_crud(id, db)

@router.put("/{id}", response_model=UsuarioOut)
def actualizar_usuario(id: int, usuarios: UsuarioCreate, db: Session = Depends(get_db)):
    return actualizar_usuario_crud(id, usuarios, db)

@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    return eliminar_usuario_crud(id, db)
