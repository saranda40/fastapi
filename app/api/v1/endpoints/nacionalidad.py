from fastapi import APIRouter, Depends, HTTPException,status
from app.schemas.usuarios import NacionalidadCreate, NacionalidadOut
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.api.v1.crud.crud_nacionalidad import crear_nacionalidad_crud, listar_nacionalidades_crud, obtener_nacionalidad_crud, actualizar_nacionalidad_crud, eliminar_nacionalidad_crud

router = APIRouter(prefix="/nacionalidad", tags=["Nacionalidad"])

@router.post("/", response_model=NacionalidadOut)
def crear_nacionalidad(nacionalidades: NacionalidadCreate, db: Session = Depends(get_db)):
    return crear_nacionalidad_crud(nacionalidades, db)

@router.get("/", response_model=List[NacionalidadOut])
def obtener_nacionalidad(db: Session = Depends(get_db)):
    return listar_nacionalidades_crud(db)

@router.get("/{id_nacionalidad}", response_model=NacionalidadOut)
def obtener_nacionalidad_por_id(id_nacionalidad: int, db: Session = Depends(get_db)):
    return obtener_nacionalidad_crud(id_nacionalidad, db)

@router.put("/{id_nacionalidad}", response_model=NacionalidadOut)
def actualizar_nacionalidad(id_nacionalidad: int, nacionalidad: NacionalidadCreate, db: Session = Depends(get_db)):
    return actualizar_nacionalidad_crud(id_nacionalidad, nacionalidad, db)

@router.delete("/{id_nacionalidad}", response_model=NacionalidadOut)
def eliminar_nacionalidad(id_nacionalidad: int, db: Session = Depends(get_db)):
    return eliminar_nacionalidad_crud(id_nacionalidad, db)