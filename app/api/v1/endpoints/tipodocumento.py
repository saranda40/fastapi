from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.usuarios import TipoDocumentoCreate, TipoDocumentoOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db
from app.api.v1.crud.crud_tipodocumento import crear_tipo_documento_crud, listar_tipos_documento_crud, obtener_tipo_documento_crud, actualizar_tipo_documento_crud, eliminar_tipo_documento_crud

router = APIRouter(prefix="/tipo_documento", tags=["Tipo Documento"])

@router.post("/", response_model=TipoDocumentoOut)
def crear_tipo_documento(tipo_documento: TipoDocumentoCreate, db: Session = Depends(get_db)):
    return crear_tipo_documento_crud(tipo_documento, db)

@router.get("/", response_model=List[TipoDocumentoOut])
def obtener_tipo_documento(db: Session = Depends(get_db)):
    return listar_tipos_documento_crud(db)

@router.get("/{id_tipo_documento}", response_model=TipoDocumentoOut)
def obtener_tipo_documento_por_id(id_tipo_documento: int, db: Session = Depends(get_db)):
    return obtener_tipo_documento_crud(id_tipo_documento, db)

@router.put("/{id_tipo_documento}", response_model=TipoDocumentoOut)
def actualizar_tipo_documento(id_tipo_documento: int, tipo_documento: TipoDocumentoCreate, db: Session = Depends(get_db)):
    return actualizar_tipo_documento_crud(id_tipo_documento, tipo_documento, db)

@router.delete("/{id_tipo_documento}", response_model=TipoDocumentoOut)
def eliminar_tipo_documento(id_tipo_documento: int, db: Session = Depends(get_db)):
    return eliminar_tipo_documento_crud(id_tipo_documento, db)