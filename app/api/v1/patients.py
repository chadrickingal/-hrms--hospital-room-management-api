from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import database
from app.services.patients import NewPatients
from app.schemas.patients import RegisterPatientsResponse, RegisterPatients


router = APIRouter()

@router.post(
        "/", 
        response_model=RegisterPatientsResponse, 
        status_code=status.HTTP_201_CREATED
    )
async def register_patient(
    patient : RegisterPatients, 
    session : AsyncSession = Depends(
        database
        )
    ):
    
    return await NewPatients.registerPatient(
        patients=patient, 
        session=session
    )