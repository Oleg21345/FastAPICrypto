# GET бере дані
# POST створює дані
# PUT оновлює
# DELETE Видаляэ
from fastapi import Body, UploadFile, File
from typing import Annotated
from src.schemas.schema.validate_data import RegisterFild
from src.schemas.schema.response_validate import UserOutId, UserOut
from fastapi import APIRouter
from src.database.metod_for_database import MetodSQL
from src.database.engine import SessionDep
import asyncio
from fastapi.responses import StreamingResponse, FileResponse

# prefix = "/"
router = APIRouter(
    tags = ["Користувачі🧑‍💻"]
)

async def sleep():
    await asyncio.sleep(3)
    print("Add to database some parametr")


@router.post("/users", summary="Реєстрація")
async def register_user(
        session: SessionDep ,user: Annotated[RegisterFild, Body()]
):
    user_add = await MetodSQL.add_user(session,user)
    return {"success": user_add}


@router.put("/users/{user_id}", summary="Змінення")
async def change_user(
        session: SessionDep ,user_id: int,user: RegisterFild
) -> bool:
    user_id = int(user_id)
    user_put = await MetodSQL.change_user(session,user_id,user)
    return user_put

@router.delete("/users/{user_id}", summary="Видалити користувача")
async def delete_user(
        session: SessionDep  ,user_id
) -> bool:
    user_id = int(user_id)
    user_delete = await MetodSQL.delete_user(session,user_id)
    return user_delete

@router.get("/users", summary="Отримати всіх користувачів")
async def get_user(session: SessionDep ) -> list[UserOut]:
    user = await MetodSQL.find_user(session)
    return user


@router.get("/users/{user_id}", summary="Отримати конкретного користувача")
async def user(session: SessionDep ,user_id: int):
    user = await MetodSQL.find_one_user(session, user_id)
    return user

