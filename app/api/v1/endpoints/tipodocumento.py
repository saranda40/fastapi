from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import TipoDocumento
from app.schemas.usuarios import TipoDocumentoCreate, TipoDocumentoBase
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.database import get_db

router = APIRouter(prefix="/tipo_documento", tags=["Tipo Documento"])

@router.post("/", response_model=TipoDocumentoBase)
def crear_tipo_documento(tipo_documento: TipoDocumentoCreate, db: Session = Depends(get_db)):
    # Validar los datos del tipo de documento
    tipo_documento = tipo_documento.tipo_documento.upper()
    activo = tipo_documento.activo

    # Verificar si el tipo de documento ya existe
    existe_tipo_documento = db.query(TipoDocumento).filter(func.lower(TipoDocumento.tipo_documento) == tipo_documento).first()
    if existe_tipo_documento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El tipo de documento ya existe")

    # Crear el nuevo tipo de documento
    nuevo_tipo_documento = TipoDocumento(tipo_documento=tipo_documento, activo=activo)
    db.add(nuevo_tipo_documento)
    db.commit()
    db.refresh(nuevo_tipo_documento)

    return nuevo_tipo_documento

@router.get("/", response_model=List[TipoDocumentoBase])
def obtener_tipo_documento(db: Session = Depends(get_db)):
    # Obtener todos los tipos de documento
    tipos_documento = db.query(TipoDocumento).all()
    return tipos_documento

@router.get("/{id_tipo_documento}", response_model=TipoDocumentoBase)
def obtener_tipo_documento_por_id(id_tipo_documento: int, db: Session = Depends(get_db)):
    # Obtener tipo de documento por ID
    tipo_documento = db.query(TipoDocumento).filter(TipoDocumento.id_tipo_documento == id_tipo_documento).first()
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")
    return tipo_documento

@router.put("/{id_tipo_documento}", response_model=TipoDocumentoBase)
def actualizar_tipo_documento(id_tipo_documento: int, tipo_documento: TipoDocumentoCreate, db: Session = Depends(get_db)):
    # Actualizar tipo de documento
    tipo_documento_db = db.query(TipoDocumento).filter(TipoDocumento.id_tipo_documento == id_tipo_documento).first()
    if not tipo_documento_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")

    tipo_documento_db.tipo_documento = tipo_documento.tipo_documento.upper()
    tipo_documento_db.activo = tipo_documento.activo
    db.commit()

    db.refresh(tipo_documento_db)
    return tipo_documento_db

@router.delete("/{id_tipo_documento}", response_model=TipoDocumentoBase)
def eliminar_tipo_documento(id_tipo_documento: int, db: Session = Depends(get_db)):
    # Eliminar tipo de documento
    tipo_documento = db.query(TipoDocumento).filter(TipoDocumento.id_tipo_documento == id_tipo_documento).first()
    if not tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de documento no encontrado")

    db.delete(tipo_documento)
    db.commit()
    return tipo_documento