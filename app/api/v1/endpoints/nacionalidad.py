from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import Nacionalidad
from app.schemas.usuarios import NacionalidadCreate, NacionalidadOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

router = APIRouter(prefix="/nacionalidad", tags=["Nacionalidad"])

@router.post("/", response_model=NacionalidadOut)
def crear_nacionalidad(nacionalidades: NacionalidadCreate, db: Session = Depends(get_db)):
    # Validar los datos de la nacionalidad
    nacionalidad_mayusc = nacionalidades.nacionalidad.upper()
    activo = nacionalidades.activo
    print(nacionalidad_mayusc)

    # Verificar si la nacionalidad ya existe
    existe_nacionalidad = db.query(Nacionalidad).filter(func.lower(Nacionalidad.nacionalidad) == nacionalidad_mayusc).first()
    if existe_nacionalidad:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La nacionalidad ya existe")

    # Crear la nueva nacionalidad
    nueva_nacionalidad = Nacionalidad(nacionalidad=nacionalidad_mayusc, activo=activo)
    db.add(nueva_nacionalidad)
    db.commit()
    db.refresh(nueva_nacionalidad)

    return nueva_nacionalidad

@router.get("/", response_model=List[NacionalidadOut])
def obtener_nacionalidad(db: Session = Depends(get_db)):
    # Obtener todas las nacionalidades
    nacionalidades = db.query(Nacionalidad).all()
    return nacionalidades

@router.get("/{id_nacionalidad}", response_model=NacionalidadOut)
def obtener_nacionalidad_por_id(id_nacionalidad: int, db: Session = Depends(get_db)):
    # Obtener nacionalidad por ID
    nacionalidad = db.query(Nacionalidad).filter(Nacionalidad.id_nacionalidad == id_nacionalidad).first()
    if not nacionalidad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nacionalidad no encontrada")
    return nacionalidad

@router.put("/{id_nacionalidad}", response_model=NacionalidadOut)
def actualizar_nacionalidad(id_nacionalidad: int, nacionalidad: NacionalidadCreate, db: Session = Depends(get_db)):
    # Actualizar nacionalidad
    nacionalidad_db = db.query(Nacionalidad).filter(Nacionalidad.id_nacionalidad == id_nacionalidad).first()
    if not nacionalidad_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nacionalidad no encontrada")

    nacionalidad_db.nacionalidad = nacionalidad.nacionalidad.lower()
    nacionalidad_db.activo = nacionalidad.activo

    db.commit()
    db.refresh(nacionalidad_db)

    return nacionalidad_db

@router.delete("/{id_nacionalidad}", response_model=NacionalidadOut)
def eliminar_nacionalidad(id_nacionalidad: int, db: Session = Depends(get_db)):
    # Eliminar nacionalidad
    nacionalidad_db = db.query(Nacionalidad).filter(Nacionalidad.id_nacionalidad == id_nacionalidad).first()
    if not nacionalidad_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nacionalidad no encontrada")

    db.delete(nacionalidad_db)
    db.commit()

    return nacionalidad_db