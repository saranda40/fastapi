from fastapi import APIRouter
from .endpoints.usuarios import router as usuarios_router
from .endpoints.estadocivil import router as estadocivil_router
from .endpoints.nacionalidad import router as nacionalidad_router
from .endpoints.tipodocumento import router as tipodocumento_router
from .endpoints.region import router as region_router
from .endpoints.comuna import router as comuna_router
from .endpoints.cargo import router as cargo_router
from .endpoints.sexo import router as sexo_router
router = APIRouter()
router.include_router(usuarios_router)
router.include_router(estadocivil_router)
router.include_router(nacionalidad_router)
router.include_router(tipodocumento_router)
router.include_router(region_router)
router.include_router(comuna_router)
router.include_router(cargo_router)
router.include_router(sexo_router)
