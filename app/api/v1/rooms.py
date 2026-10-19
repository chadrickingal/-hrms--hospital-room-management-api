from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.rooms import CreateNewRoom
from app.schemas.rooms import CreateRoom, CreateRoomResponse
from app.core.database import database


router = APIRouter()

@router.post(
    "/", 
    response_model=CreateRoomResponse, 
    status_code=status.HTTP_201_CREATED
    )
async def add_room(
    new_room : CreateRoom, 
    session : AsyncSession = Depends(
        database
        )
    ):

    return await CreateNewRoom.create_room(new_room=new_room, session=session)

