from fastapi import APIRouter
from .endpoints import usuarios, estadocivil, nacionalidad, tipodocumento, region, comuna, cargo, sexo

router = APIRouter()
router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
router.include_router(estadocivil.router, prefix="/estadocivil", tags=["Estado Civil"])
router.include_router(nacionalidad.router, prefix="/nacionalidad", tags=["Nacionalidad"])
router.include_router(tipodocumento.router, prefix="/tipodocumento", tags=["Tipo Documento"])
router.include_router(region.router, prefix="/region", tags=["Región"])
router.include_router(comuna.router, prefix="/comuna", tags=["Comuna"])
router.include_router(cargo.router, prefix="/cargo", tags=["Cargo"])
router.include_router(sexo.router, prefix="/sexo", tags=["Sexo"])
