
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, status

from app.models.rooms import Rooms
from app.schemas.rooms import CreateRoom

class CreateNewRoom:
    @staticmethod
    async def create_room(new_room: CreateRoom, session : AsyncSession):
       
        room = Rooms(
            room_no = f"RN-{new_room.room_no}",
            room_status = new_room.room_status,
            room_floor = new_room.room_floor,
            room_types = new_room.room_types,
        )

        session.add(room)

        try: 
            await session.commit()
            await session.refresh(room)
            return room

        except IntegrityError:

            await session.rollback()
            
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="room is already exist!"
            )
  