from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.usuarios import SexoCreate, SexoOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.api.v1.crud.crud_sexo import crear_sexo_crud, listar_sexos_crud, obtener_sexo_crud, actualizar_sexo_crud, eliminar_sexo_crud

router = APIRouter(prefix="/sexo", tags=["Sexo"])

@router.post("/", response_model=SexoOut)
def crear_sexo(sexo: SexoCreate, db: Session = Depends(get_db)):
    return crear_sexo_crud(sexo, db)

@router.get("/", response_model=List[SexoOut])
def obtener_sexo(db: Session = Depends(get_db)):
    return listar_sexos_crud(db)

@router.get("/{id_sexo}", response_model=SexoOut)
def obtener_sexo_por_id(id_sexo: int, db: Session = Depends(get_db)):
    return obtener_sexo_crud(id_sexo, db)

@router.put("/{id_sexo}", response_model=SexoOut)
def actualizar_cargo(id_sexo: int, cargo: SexoCreate, db: Session = Depends(get_db)):
    return actualizar_sexo_crud(id_sexo, cargo, db)

@router.delete("/{id_sexo}", response_model=SexoOut)
def eliminar_sexo(id_sexo: int, db: Session = Depends(get_db)):
    return eliminar_sexo_crud(id_sexo, db)
