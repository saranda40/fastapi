from pydantic import BaseModel, EmailStr
from datetime import date, datetime

class UsuarioBase(BaseModel):
    usuario: str
    email: EmailStr
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    numero_documento: str
    id_tipo_documento: int
    id_estado_civil: int
    id_nacionalidad: int
    id_cargo: int
    telefono: str
    id_sexo: int
    direccion: str  
    id_region: int
    id_comuna: int

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    id_usuario: int
    creado_en: datetime

    class Config:
        orm_mode = True

class EstadoCivilBase(BaseModel):
    estado_civil: str
    activo: bool

class EstadoCivilCreate(EstadoCivilBase):
    pass

class EstadoCivilOut(EstadoCivilBase):
    id_estado_civil: int

    class Config:
        orm_mode = True

class NacionalidadBase(BaseModel):
    nacionalidad: str
    activo: bool

class NacionalidadCreate(NacionalidadBase):
    pass

class NacionalidadOut(NacionalidadBase):
    id_nacionalidad: int

    class Config:
        orm_mode = True

class TipoDocumentoBase(BaseModel):
    tipo_documento: str
    activo: bool

class TipoDocumentoCreate(TipoDocumentoBase):
    pass

class TipoDocumentoOut(TipoDocumentoBase):
    id_tipo_documento: int

    class Config:
        orm_mode = True

class RegionBase(BaseModel):
    region: str
    activo: bool
class RegionCreate(RegionBase):
    pass
class RegionOut(RegionBase):
    id_region: int

    class Config:
        orm_mode = True

class ComunaBase(BaseModel):
    comuna: str
    activo: bool
    id_region: int
class ComunaCreate(ComunaBase):
    pass
class ComunaOut(ComunaBase):
    id_comuna: int

    class Config:
        orm_mode = True
        
class CargoBase(BaseModel):
    cargo: str
    activo: bool
class CargoCreate(CargoBase):
    pass
class CargoOut(CargoBase):
    id_cargo: int

    class Config:
        orm_mode = True
class SexoBase(BaseModel):
    sexo: str
    activo: bool
class SexoCreate(SexoBase):
    pass
class SexoOut(SexoBase):
    id_sexo: int

    class Config:
        orm_mode = True
