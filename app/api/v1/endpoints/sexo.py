from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Sexo
from app.schemas.usuarios import SexoCreate, SexoOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

router = APIRouter(prefix="/sexo", tags=["Sexo"])

@router.post("/", response_model=SexoOut)
def crear_sexo(sexo: SexoCreate, db: Session = Depends(get_db)):
    # Validar los datos del sexo
    sexo = sexo.sexo.upper()
    activo = sexo.activo

    # Verificar si el sexo ya existe
    existe_sexo = db.query(Sexo).filter(func.lower(Sexo.sexo) == sexo).first()
    if existe_sexo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sexo ya existe")

    # Crear el nuevo sexo
    nuevo_sexo = Sexo(sexo=sexo, activo=activo)
    db.add(nuevo_sexo)
    db.commit()
    db.refresh(nuevo_sexo)

    return nuevo_sexo

@router.get("/", response_model=List[SexoOut])
def obtener_sexo(db: Session = Depends(get_db)):
    # Obtener todos los sexos           
    sexos = db.query(Sexo).all()
    return sexos

@router.get("/{id_sexo}", response_model=SexoOut)
def obtener_sexo_por_id(id_sexo: int, db: Session = Depends(get_db)):
    # Obtener cargo por ID
    sexo = db.query(Sexo).filter(Sexo.id_sexo == id_sexo).first()
    if not sexo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sexo no encontrado")
    return sexo

@router.put("/{id_sexo}", response_model=SexoOut)
def actualizar_cargo(id_sexo: int, cargo: SexoCreate, db: Session = Depends(get_db)):
    # Actualizar cargo
    sexo_db = db.query(Sexo).filter(Sexo.id_sexo == id_sexo).first()
    if not sexo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sexo no encontrado")

    sexo_db.cargo = cargo.cargo.upper()
    sexo_db.activo = cargo.activo
    db.commit()
    db.refresh(sexo_db)

    return sexo_db

@router.delete("/{id_sexo}", response_model=SexoOut)
def eliminar_sexo(id_sexo: int, db: Session = Depends(get_db)):
    # Eliminar cargo
    sexo_db = db.query(Sexo).filter(Sexo.id_sexo == id_sexo).first()
    if not sexo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sexo no encontrado")

    db.delete(sexo_db)
    db.commit()

    return sexo_db
