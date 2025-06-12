from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Comuna
from app.schemas.usuarios import ComunaCreate, ComunaOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

def crear_comuna_crud(comunas: ComunaCreate, db: Session = Depends(get_db)):
     # Validar los datos de la comuna
    comuna = comunas.comuna.upper()
    activo = comunas.activo
    id_region = comunas.id_region

    # Verificar si la comuna ya existe
    existe_comuna = db.query(Comuna).filter(func.lower(Comuna.comuna) == comuna).first()
    if existe_comuna:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La comuna ya existe")
    
    # Verificar si la región existe
    existe_region = db.query(Comuna).filter(Comuna.id_region == id_region).first()
    if not existe_region:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La región no existe")
    # Verificar si la comuna pertenece a la región
    comuna_region = db.query(Comuna).filter(Comuna.id_region == id_region, func.lower(Comuna.comuna) == comuna).first()
    if comuna_region:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La comuna ya pertenece a la región")
    # Verificar si la comuna pertenece a otra región
    comuna_otra_region = db.query(Comuna).filter(Comuna.id_region != id_region, func.lower(Comuna.comuna) == comuna).first()
    if comuna_otra_region:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La comuna ya pertenece a otra región")

    # Crear la nueva comuna
    nueva_comuna = Comuna(comuna=comuna, activo=activo, id_region=id_region)
    db.add(nueva_comuna)
    db.commit()
    db.refresh(nueva_comuna)

def listar_comunas_crud(id_region: int, db: Session = Depends(get_db)):
    # Obtener todas las comunas
    comunas = db.query(Comuna).filter(Comuna.id_region == id_region).all()
    return comunas

def obtener_comuna_crud(id_comuna: int, db: Session = Depends(get_db)):
    # Obtener comuna por ID
    comuna = db.query(Comuna).filter(Comuna.id_comuna == id_comuna).first()
    if not comuna:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comuna no encontrada")
    return comuna

def actualizar_comuna_crud(id_comuna: int, comuna: ComunaCreate, db: Session = Depends(get_db)):
    # Actualizar comuna
    comuna_db = db.query(Comuna).filter(Comuna.id_comuna == id_comuna).first()
    if not comuna_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comuna no encontrada")

    comuna_db.comuna = comuna.comuna.upper()
    comuna_db.id_region = comuna.id_region
    comuna_db.activo = comuna.activo
    db.commit()
    db.refresh(comuna_db)

    return comuna_db

def eliminar_comuna_crud(id_comuna: int, db: Session = Depends(get_db)):
    # Eliminar comuna
    comuna_db = db.query(Comuna).filter(Comuna.id_comuna == id_comuna).first()
    if not comuna_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comuna no encontrada")

    db.delete(comuna_db)
    db.commit()

    return {"detail": "Comuna eliminada exitosamente"}