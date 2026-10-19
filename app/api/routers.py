from fastapi import APIRouter

from app.api.v1.rooms import router as rooms
from app.api.v1.patients import router as patients
from app.api.v1.admission import router as admission

router = APIRouter()

router.include_router(
    rooms,
    prefix="/rooms",
    tags=["Rooms"],
)

router.include_router(
    patients,
    prefix="/patients",
    tags=["Patients"]
)

router.include_router(
    admission,
    prefix="/admissions",
    tags=["Admissions"]
)