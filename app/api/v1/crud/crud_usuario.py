from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.models.usuarios import Usuario, EstadoCivil, Nacionalidad, TipoDocumento, Region, Comuna, Cargo, Sexo
from app.schemas.usuarios import UsuarioCreate
from typing import List
from sqlalchemy import func
from app.util import encriptar_contraseña
from app.database import get_db

def crear_usuario_crud(usuarios: UsuarioCreate, db: Session = Depends(get_db)):
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

def listar_usuarios_crud(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

def obtener_usuario_crud(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

def actualizar_usuario_crud(id: int, datos: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.nombres = datos.nombres
    usuario.email = datos.email
    usuario.password = encriptar_contraseña(datos.password)
    usuario.apellidos = datos.apellidos
    usuario.numero_documento = datos.numero_documento
    usuario.id_tipo_documento = datos.id_tipo_documento
    usuario.id_estado_civil = datos.id_estado_civil
    usuario.id_nacionalidad = datos.id_nacionalidad 
    usuario.id_cargo = datos.id_cargo
    usuario.fecha_nacimiento = datos.fecha_nacimiento
    usuario.telefono = datos.telefono
    usuario.id_sexo = datos.id_sexo
    usuario.direccion = datos.direccion
    usuario.id_region = datos.id_region
    usuario.id_comuna = datos.id_comuna
    db.commit()
    return usuario

def eliminar_usuario_crud(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"ok": True}