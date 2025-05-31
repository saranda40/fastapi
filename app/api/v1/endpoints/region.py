from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Region
from app.schemas.usuarios import RegionCreate, RegionOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.api.v1.crud.crud_region import crear_region_crud, listar_regiones_crud, obtener_region_crud, actualizar_region_crud, eliminar_region_crud

router = APIRouter(prefix="/region", tags=["Región"])

@router.post("/", response_model=RegionOut)
def crear_region(regiones: RegionCreate, db: Session = Depends(get_db)):
    return crear_region_crud(regiones, db)

@router.get("/", response_model=List[RegionOut])
def obtener_region(db: Session = Depends(get_db)):
    return listar_regiones_crud(db)

@router.get("/{id_region}", response_model=RegionOut)
def obtener_region_por_id(id_region: int, db: Session = Depends(get_db)):
    return obtener_region_crud(id_region, db)

@router.put("/{id_region}", response_model=RegionOut)
def actualizar_region(id_region: int, region: RegionCreate, db: Session = Depends(get_db)):
    return actualizar_region_crud(id_region, region, db)

@router.delete("/{id_region}", response_model=RegionOut)
def eliminar_region(id_region: int, db: Session = Depends(get_db)):
    return eliminar_region_crud(id_region, db)