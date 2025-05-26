from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import Usuario, EstadoCivil, Nacionalidad, TipoDocumento, Region, Comuna, Cargo, Sexo
from app.schemas.usuarios import UsuarioCreate, UsuarioOut
from app.database import SessionLocal
from typing import List
from sqlalchemy import func
from app.util import encriptar_contraseña
from app.database import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioOut)
def crear_usuario(usuarios: UsuarioCreate, db: Session = Depends(get_db)):
    # Validar los datos del usuario

    usuario = usuarios.usuario.lower()
    email = usuarios.email.lower()
    contraseña_encriptada = encriptar_contraseña(usuarios.password)
    nombres = usuarios.nombres.lower()
    apellidos = usuarios.apellidos.lower()
    numero_documento = usuarios.numero_documento
    id_tipo_documento = usuarios.id_tipo_documento
    id_estado_civil= usuarios.id_estado_civil
    id_nacionalidad= usuarios.id_nacionalidad
    id_cargo= usuarios.id_cargo
    fecha_nacimiento = usuarios.fecha_nacimiento
    telefono = usuarios.telefono
    id_sexo = usuarios.id_sexo
    direccion = usuarios.direccion
    id_region = usuarios.id_region
    id_comuna = usuarios.id_comuna


    valida_estado_civil = db.query(EstadoCivil).filter(EstadoCivil.id_estado_civil == id_estado_civil and EstadoCivil.activo == True).first()
    if not valida_estado_civil:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El estado civil no existe")
    
    valida_nacionalidad = db.query(Nacionalidad).filter(Nacionalidad.id_nacionalidad == id_nacionalidad and Nacionalidad.activo == True).first()
    if not valida_nacionalidad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La nacionalidad no existe")
    
    valida_tipo_documento = db.query(TipoDocumento).filter(TipoDocumento.id_tipo_documento == id_tipo_documento and TipoDocumento.activo == True).first()
    if not valida_tipo_documento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El tipo de documento no existe")
    
    valida_region = db.query(Region).filter(Region.id_region == id_region and Region.activo == True).first()
    if not valida_region:   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La región no existe")
    
    valida_comuna = db.query(Comuna).filter(Comuna.id_comuna == id_comuna and Comuna.activo == True).first()
    if not valida_comuna:   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La comuna no existe")
    
    valida_cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo and Cargo.activo == True).first()
    if not valida_cargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El cargo no existe")
    
    valida_sexo = db.query(Sexo).filter(Sexo.id_sexo == id_sexo and Sexo.activo == True).first()
    if not valida_sexo:  
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El sexo no existe")

    # Verificar si el email ya existe
    email_existente = db.query(Usuario).filter(func.lower(Usuario.email) == email).first()
    if email_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El email ya existe")

    nuevo = Usuario(
        usuario=usuario,
        email=email,
        password=contraseña_encriptada,
        nombres=nombres,
        apellidos=apellidos,
        numero_documento=numero_documento,
        id_tipo_documento=id_tipo_documento,
        id_estado_civil= id_estado_civil,
        id_nacionalidad= id_nacionalidad,
        id_cargo= id_cargo,
        telefono = telefono,
        fecha_nacimiento =fecha_nacimiento,
        id_sexo = id_sexo,
        direccion = direccion,
        id_region = id_region,
        id_comuna = id_comuna,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/{id}", response_model=UsuarioOut)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{id}", response_model=UsuarioOut)
def actualizar_usuario(id: int, datos: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.nombres = datos.nombres
    usuario.email = datos.email
    usuario.contraseña = datos.contraseña
    db.commit()
    return usuario

@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"ok": True}
