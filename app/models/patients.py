from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.base import Base

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.admissions import Admissions

class Patients(Base):

    __tablename__="patients"

    patients_no : Mapped[str] = mapped_column(
        String,
        primary_key=True,
        index=True
    )

    patients_name : Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    admission : Mapped[list["Admissions"]] = relationship(
        back_populates="patient"
    )