from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.usuarios import ComunaCreate, ComunaOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.api.v1.crud.crud_comuna import crear_comuna_crud, listar_comunas_crud, obtener_comuna_crud, actualizar_comuna_crud, eliminar_comuna_crud

router = APIRouter(prefix="/comuna", tags=["Comuna"])

@router.post("/", response_model=ComunaOut)
def crear_comuna(comunas: ComunaCreate, db: Session = Depends(get_db)):
    return crear_comuna_crud(comunas, db)

@router.get("/{id_region}", response_model=List[ComunaOut])
def obtener_comuna(id_region: int, db: Session = Depends(get_db)):
    return listar_comunas_crud(id_region, db)

@router.get("/{id_comuna}", response_model=ComunaOut)
def obtener_comuna_por_id(id_comuna: int, db: Session = Depends(get_db)):
    return obtener_comuna_crud(id_comuna, db)

@router.put("/{id_comuna}", response_model=ComunaOut)
def actualizar_comuna(id_comuna: int, comuna: ComunaCreate, db: Session = Depends(get_db)):
    return actualizar_comuna_crud(id_comuna, comuna, db)

@router.delete("/{id_comuna}", response_model=ComunaOut)
def eliminar_comuna(id_comuna: int, db: Session = Depends(get_db)):
    return eliminar_comuna_crud(id_comuna, db)

