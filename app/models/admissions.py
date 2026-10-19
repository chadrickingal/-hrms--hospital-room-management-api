from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, time
from app.core.base import Base

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.rooms import Rooms
    from app.models.patients import Patients

from sqlalchemy import (
    String, 
    Integer, 
    DATE, 
    TIME,
    ForeignKey,
)
class Admissions(Base):
    __tablename__="admissions"

    admission_no : Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    room_no : Mapped[str] = mapped_column(
        ForeignKey("rooms.room_no"),
        nullable=False
    )

    patient_no : Mapped[str] = mapped_column(
        ForeignKey("patients.patients_no"),
        nullable=False
    )

    status : Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="active"
    )

    admitted_time : Mapped[time] = mapped_column(
        TIME,
        nullable=False
    )

    admitted_date : Mapped[date] = mapped_column(
        DATE,
        nullable=False
    )

    discharge_time : Mapped[time] = mapped_column(
        TIME,
        nullable=False
    )
    
    discharge_date : Mapped[date] = mapped_column(
        DATE,
        nullable=False
    )

    patient : Mapped["Patients"] = relationship(
        back_populates="admission"
    )

    room : Mapped["Rooms"] = relationship(
        back_populates="admission"
    )