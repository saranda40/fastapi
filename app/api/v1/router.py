from fastapi import APIRouter
from .endpoints import usuarios, estadocivil, nacionalidad, tipodocumento, region, comuna, cargo, sexo

router = APIRouter()
router.include_router(usuarios.router, tags=["Usuarios"])
router.include_router(estadocivil.router, tags=["Estado Civil"])
router.include_router(nacionalidad.router, tags=["Nacionalidad"])
router.include_router(tipodocumento.router, tags=["Tipo Documento"])
router.include_router(region.router, tags=["Región"])
router.include_router(comuna.router, tags=["Comuna"])
router.include_router(cargo.router, tags=["Cargo"])
router.include_router(sexo.router, tags=["Sexo"])
