from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/health")
async def get_health() -> JSONResponse:
    """
    Заглушка метода health
    """

    return JSONResponse({"status": "OK"})
