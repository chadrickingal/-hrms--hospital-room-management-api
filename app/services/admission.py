
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, status

from app.schemas.admissions import AdmissionsRooms
from app.models.admissions import Admissions


class NewAdmitted:

    @staticmethod
    async def assign_patient_room(admit : AdmissionsRooms, session : AsyncSession):
        patient_admission = Admissions(
            patient_no = f"AN-{admit.patient_no}",
            room_no = admit.room_no,
            admitted_time = admit.admitted_time,
            admitted_date = admit.admitted_date,
            discharge_time = admit.discharge_time,
            discharge_date = admit.discharge_date,
            status = admit.status
        )

        session.add(patient_admission)

        try:
            session.commit()
            session.refresh(patient_admission)
            return patient_admission
        except IntegrityError:
            session.rollback()

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="room already assigned"
            )