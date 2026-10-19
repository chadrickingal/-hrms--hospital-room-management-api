from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import database
from app.services.admission import NewAdmitted
from app.schemas.admissions import AdmissionsRooms, AdmissionRoomsResponse


router = APIRouter()

@router.post(
        "/", 
        response_model=AdmissionRoomsResponse, 
        status_code=status.HTTP_201_CREATED
    )
async def assign_patient_room(
    assign : AdmissionsRooms, 
    session : AsyncSession = Depends(database)
):
    return await NewAdmitted.assign_patient_room(
        admit=assign, 
        session=session
        )