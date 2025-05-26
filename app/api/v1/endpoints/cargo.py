from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Cargo
from app.schemas.usuarios import CargoCreate, CargoOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

router = APIRouter(prefix="/cargo", tags=["Cargo"])
# Dependencia para obtener DB

@router.post("/", response_model=CargoOut)
def crear_cargos(Cargos: CargoCreate, db: Session = Depends(get_db)):
    # Validar los datos de la cargo
    cargo = Cargos.cargo.upper()
    activo = Cargos.activo

    # Verificar si la cargo ya existe
    existe_cargo= db.query(Cargo).filter(func.lower(Cargo.cargo) == cargo).first()
    if existe_cargo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cargo ya existe")

    # Crear la nueva cargo
    nuevo_cargo = Cargo(cargo=cargo, activo=activo)
    db.add(nuevo_cargo)
    db.commit()
    db.refresh(nuevo_cargo)

    return nuevo_cargo

@router.get("/", response_model=List[CargoOut])
def obtener_cargos(db: Session = Depends(get_db)):
    # Obtener todas los Cargos
    cargos = db.query(Cargo).all()
    return cargos

@router.get("/{id_cargo}", response_model=CargoOut)
def obtener_cargo_por_id(id_cargo: int, db: Session = Depends(get_db)):
    # Obtener cargo por ID
    cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo no encontrado")
    return cargo

@router.put("/{id_cargo}", response_model=CargoOut)
def actualizar_cargo(id_cargo: int, cargo: CargoCreate, db: Session = Depends(get_db)):
    # Actualizar cargo
    cargo_db = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo no encontrado")

    cargo_db.cargo = cargo.cargo.upper()
    cargo_db.activo = cargo.activo
    db.commit()
    db.refresh(cargo_db)

    return cargo_db

@router.delete("/{id_cargo}", response_model=CargoOut)
def eliminar_cargo(id_cargo: int, db: Session = Depends(get_db)):
    # Eliminar cargo
    cargo_db = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cargo no encontrado")

    db.delete(cargo_db)
    db.commit()

    return cargo_db





