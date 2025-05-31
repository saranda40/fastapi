from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.usuarios import CargoCreate, CargoOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.api.v1.crud.crud_cargo import crear_cargo_crud, listar_cargos_crud, obtener_cargo_crud, actualizar_cargo_crud, eliminar_cargo_crud
from app.database import get_db

router = APIRouter(prefix="/cargo", tags=["Cargo"])

@router.post("/", response_model=CargoOut)
def crear_cargos(Cargos: CargoCreate, db: Session = Depends(get_db)):
    return crear_cargo_crud(Cargos, db)

@router.get("/", response_model=List[CargoOut])
def obtener_cargos(db: Session = Depends(get_db)):
    return listar_cargos_crud(db)

@router.get("/{id_cargo}", response_model=CargoOut)
def obtener_cargo_por_id(id_cargo: int, db: Session = Depends(get_db)):
    return obtener_cargo_crud(id_cargo, db)

@router.put("/{id_cargo}", response_model=CargoOut)
def actualizar_cargo(id_cargo: int, cargo: CargoCreate, db: Session = Depends(get_db)):
    return actualizar_cargo_crud(id_cargo, cargo, db)

@router.delete("/{id_cargo}", response_model=CargoOut)
def eliminar_cargo(id_cargo: int, db: Session = Depends(get_db)):
    return eliminar_cargo_crud(id_cargo, db)





