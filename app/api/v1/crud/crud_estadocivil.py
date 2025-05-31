from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import EstadoCivil
from app.schemas.usuarios import EstadoCivilCreate, EstadoCivilOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

def crear_estado_civil_crud(estado_civil: EstadoCivilCreate, db: Session = Depends(get_db)):
    # Validar los datos del estado civil
    estado_civil = estado_civil.estado_civil.lower()
    activo = estado_civil.activo

    # Verificar si el estado civil ya existe
    existe_estado_civil = db.query(EstadoCivil).filter(func.lower(EstadoCivil.estado_civil) == estado_civil).first()
    if existe_estado_civil:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El estado civil ya existe")

    # Crear el nuevo estado civil
    nuevo_estado_civil = EstadoCivil(estado_civil=estado_civil, activo=activo)
    db.add(nuevo_estado_civil)
    db.commit()
    db.refresh(nuevo_estado_civil)

    return nuevo_estado_civil

def listar_estados_civiles_crud(db: Session = Depends(get_db)):
    # Obtener todos los estados civiles
    estados_civiles = db.query(EstadoCivil).all()
    return estados_civiles

def obtener_estado_civil_crud(id_estado_civil: int, db: Session = Depends(get_db)):
    # Obtener estado civil por ID
    estado_civil = db.query(EstadoCivil).filter(EstadoCivil.id_estado_civil == id_estado_civil).first()
    if not estado_civil:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado civil no encontrado")
    return estado_civil

def actualizar_estado_civil_crud(id_estado_civil: int, estado_civil: EstadoCivilCreate, db: Session = Depends(get_db)):
    # Actualizar estado civil
    estado_civil_db = db.query(EstadoCivil).filter(EstadoCivil.id_estado_civil == id_estado_civil).first()
    if not estado_civil_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado civil no encontrado")

    estado_civil_db.estado_civil = estado_civil.estado_civil.lower()
    estado_civil_db.activo = estado_civil.activo
    db.commit()
    db.refresh(estado_civil_db)

    return estado_civil_db

def eliminar_estado_civil_crud(id_estado_civil: int, db: Session = Depends(get_db)):
    # Eliminar estado civil
    estado_civil_db = db.query(EstadoCivil).filter(EstadoCivil.id_estado_civil == id_estado_civil).first()
    if not estado_civil_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado civil no encontrado")

    db.delete(estado_civil_db)
    db.commit()

    return estado_civil_db
