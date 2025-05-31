from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import  Sexo
from app.schemas.usuarios import SexoCreate
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

def crear_sexo_crud(sexo: SexoCreate, db: Session = Depends(get_db)):
    # Validar los datos del sexo
    sexo_nombre = sexo.sexo.upper() # Convertir a mayúsculas
    activo = sexo.activo

    # Verificar si el sexo ya existe
    existe_sexo = db.query(Sexo).filter(func.lower(Sexo.sexo) == sexo_nombre).first()
    if existe_sexo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sexo ya existe")

    # Crear el nuevo sexo
    nuevo_sexo = Sexo(sexo=sexo_nombre, activo=activo)
    db.add(nuevo_sexo)
    db.commit()
    db.refresh(nuevo_sexo)

    return nuevo_sexo

def listar_sexos_crud(db: Session = Depends(get_db)):
    # Obtener todos los sexos
    sexos = db.query(Sexo).all()
    return sexos

def obtener_sexo_crud(id_sexo: int, db: Session = Depends(get_db)):
    # Obtener sexo por ID
    sexo = db.query(Sexo).filter(Sexo.id_sexo == id_sexo).first()
    if not sexo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sexo no encontrado")
    return sexo

def actualizar_sexo_crud(id_sexo: int, sexo: SexoCreate, db: Session = Depends(get_db)):
    # Actualizar sexo
    sexo_db = db.query(Sexo).filter(Sexo.id_sexo == id_sexo).first()
    if not sexo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sexo no encontrado")

    sexo_db.sexo = sexo.sexo.upper()
    sexo_db.activo = sexo.activo
    db.commit()
    db.refresh(sexo_db)

    return sexo_db

def eliminar_sexo_crud(id_sexo: int, db: Session = Depends(get_db)):
    # Eliminar sexo
    sexo_db = db.query(Sexo).filter(Sexo.id_sexo == id_sexo).first()
    if not sexo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sexo no encontrado")

    db.delete(sexo_db)
    db.commit()

    return sexo_db