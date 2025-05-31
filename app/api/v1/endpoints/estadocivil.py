from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.usuarios import EstadoCivilCreate, EstadoCivilOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.api.v1.crud.crud_estadocivil import crear_estado_civil_crud, listar_estados_civiles_crud, obtener_estado_civil_crud, actualizar_estado_civil_crud, eliminar_estado_civil_crud

router = APIRouter(prefix="/estado_civil", tags=["Estado Civil"])

@router.post("/", response_model=EstadoCivilOut)
def crear_estado_civil(estado_civil: EstadoCivilCreate, db: Session = Depends(get_db)):
    return crear_estado_civil_crud(estado_civil, db)

@router.get("/", response_model=List[EstadoCivilOut])
def obtener_estado_civil(db: Session = Depends(get_db)):
    return listar_estados_civiles_crud(db)

@router.get("/{id_estado_civil}", response_model=EstadoCivilOut)
def obtener_estado_civil_por_id(id_estado_civil: int, db: Session = Depends(get_db)):
    return obtener_estado_civil_crud(id_estado_civil, db)

@router.put("/{id_estado_civil}", response_model=EstadoCivilOut)
def actualizar_estado_civil(id_estado_civil: int, estado_civil: EstadoCivilCreate, db: Session = Depends(get_db)):
    return actualizar_estado_civil_crud(id_estado_civil, estado_civil, db)

@router.delete("/{id_estado_civil}", response_model=EstadoCivilOut)
def eliminar_estado_civil(id_estado_civil: int, db: Session = Depends(get_db)):
    return eliminar_estado_civil_crud(id_estado_civil, db)
