from pydantic import BaseModel, ConfigDict


class CreateRoom(BaseModel):
    room_no : int
    room_status : str
    room_floor : str
    room_types : str

class CreateRoomResponse(BaseModel):

    room_no : str
    room_status : str
    room_floor : str
    room_types : str

    model_config = ConfigDict(from_attributes=True)

