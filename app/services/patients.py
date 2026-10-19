from app.schemas.patients import RegisterPatients
from app.models.patients import Patients


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, status

class NewPatients:

    @staticmethod
    async def registerPatient(patients : RegisterPatients, session : AsyncSession):

        patient = Patients(
            patients_no = f"PN-{patients.patients_no}",
            patients_name = patients.patients_name,
        )

        session.add(patient)

        try:
            await session.commit()
            await session.refresh(patient)
            return {"msg":"successfully saved"}
        except IntegrityError:
            await session.rollback()

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="patient already exist"
            )