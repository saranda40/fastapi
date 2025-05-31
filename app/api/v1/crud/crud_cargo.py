from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Cargo
from app.schemas.usuarios import CargoCreate
from typing import List
from sqlalchemy import func
from app.util import encriptar_contraseña
from app.database import get_db

def crear_cargo_crud(cargo: CargoCreate, db: Session = Depends(get_db)):
    # Validar los datos del cargo
    cargo_nombre = cargo.cargo.lower()
    activo = cargo.activo

    # Verificar si el cargo ya existe
    existe_cargo = db.query(Cargo).filter(func.lower(Cargo.cargo) == cargo_nombre).first()
    if existe_cargo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El cargo ya existe")

    # Crear el nuevo cargo
    nuevo_cargo = Cargo(cargo=cargo_nombre, activo=activo)
    db.add(nuevo_cargo)
    db.commit()
    db.refresh(nuevo_cargo)

    return nuevo_cargo

def listar_cargos_crud(db: Session = Depends(get_db)):
    # Obtener todos los cargos
    cargos = db.query(Cargo).all()
    return cargos

def obtener_cargo_crud(id_cargo: int, db: Session = Depends(get_db)):
    # Obtener cargo por ID
    cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo no encontrado")
    return cargo

def actualizar_cargo_crud(id_cargo: int, cargo: CargoCreate, db: Session = Depends(get_db)):
    # Actualizar cargo
    cargo_db = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo no encontrado")

    cargo_db.cargo = cargo.cargo.upper()
    cargo_db.activo = cargo.activo
    db.commit()
    db.refresh(cargo_db)

    return cargo_db

def eliminar_cargo_crud(id_cargo: int, db: Session = Depends(get_db)):
    # Eliminar cargo
    cargo_db = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo no encontrado")

    db.delete(cargo_db)
    db.commit()

    return cargo_db 
