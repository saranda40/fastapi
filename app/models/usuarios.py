from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ =  "Usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    activo = Column(String(1), nullable=False,server_default='S')
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    numero_documento = Column(String(20), nullable=False)
    id_tipo_documento = Column(Integer, nullable=False)
    id_estado_civil = Column(Integer, nullable=False)
    id_nacionalidad = Column(Integer, nullable=False)
    id_cargo = Column(Integer, nullable=False)
    telefono = Column(String(20), nullable=False)                                                                                                            
    fecha_nacimiento = Column(DateTime(timezone=True), nullable=False)
    id_sexo = Column(Integer, nullable=False)
    direccion = Column(String(255), nullable=False)
    id_region = Column(Integer, nullable=False)
    id_comuna = Column(Integer, nullable=False)

class EstadoCivil(Base):
    __tablename__ = "Estado_civil"

    id_estado_civil = Column(Integer, primary_key=True, index=True)
    estado_civil = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

class Nacionalidad(Base):
    __tablename__ = "Nacionalidad"

    id_nacionalidad = Column(Integer, primary_key=True, index=True)
    nacionalidad = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

class TipoDocumento(Base):
    __tablename__ = "Tipo_documento"

    id_tipo_documento = Column(Integer, primary_key=True, index=True)
    tipo_documento = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

class Region(Base):
    __tablename__ = "Regiones"

    id_region = Column(Integer, primary_key=True, index=True)
    region = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

class Comuna(Base):
    __tablename__ = "Comunas"

    id_comuna = Column(Integer, primary_key=True, index=True)
    comuna = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)
    id_region = Column(Integer, nullable=False)

class Cargo(Base):
    __tablename__ = "Cargos"

    id_cargo = Column(Integer, primary_key=True, index=True)
    cargo = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

class Sexo(Base):
    __tablename__ = "Sexo"

    id_sexo = Column(Integer, primary_key=True, index=True)
    sexo = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)