from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Region
from app.schemas.usuarios import RegionCreate, RegionOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

router = APIRouter(prefix="/region", tags=["Región"])

@router.post("/", response_model=RegionOut)
def crear_region(regiones: RegionCreate, db: Session = Depends(get_db)):
    # Validar los datos de la region
    region = regiones.region.upper()
    activo = regiones.activo

    # Verificar si la region ya existe
    existe_region = db.query(Region).filter(func.lower(Region.region) == region).first()
    if existe_region:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La region ya existe")

    # Crear la nueva region
    nueva_region = Region(region=region, activo=activo)
    db.add(nueva_region)
    db.commit()
    db.refresh(nueva_region)

    return nueva_region

@router.get("/", response_model=List[RegionOut])
def obtener_region(db: Session = Depends(get_db)):
    # Obtener todas las regiones
    regiones = db.query(Region).all()
    return regiones

@router.get("/{id_region}", response_model=RegionOut)
def obtener_region_por_id(id_region: int, db: Session = Depends(get_db)):
    # Obtener region por ID
    region = db.query(Region).filter(Region.id_region == id_region).first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Region no encontrada")
    return region

@router.put("/{id_region}", response_model=RegionOut)
def actualizar_region(id_region: int, region: RegionCreate, db: Session = Depends(get_db)):
    # Actualizar region
    region_db = db.query(Region).filter(Region.id_region == id_region).first()
    if not region_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Region no encontrada")

    region_db.region = region.region.upper()
    region_db.activo = region.activo
    db.commit()
    db.refresh(region_db)

    return region_db

@router.delete("/{id_region}", response_model=RegionOut)
def eliminar_region(id_region: int, db: Session = Depends(get_db)):
    # Eliminar region
    region_db = db.query(Region).filter(Region.id_region == id_region).first()
    if not region_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Region no encontrada")

    db.delete(region_db)
    db.commit()

    return region_db