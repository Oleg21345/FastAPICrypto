from fastapi import APIRouter
from src.app.router import router as router_main
from src.app.router_authorization import router as router_auto
from src.app.router_for_files import router as router_files



global_router = APIRouter(

)

global_router.include_router(router_main)
global_router.include_router(router_auto)
global_router.include_router(router_files)
