from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.admissions import Admissions

class Rooms(Base):
    __tablename__ = "rooms"

    room_no : Mapped[str] = mapped_column(
        String, 
        primary_key=True, 
        index=True, 
        nullable=False)
    
    room_status : Mapped[str] = mapped_column(
        String, 
        nullable=False, 
        default="vacant", 
        index=True)
    
    room_floor : Mapped[str] = mapped_column(
        String, 
        nullable=False)
    
    room_types : Mapped[str] = mapped_column(
        String, 
        nullable=False)

    admission : Mapped[list["Admissions"]] = relationship(
        back_populates="room"
    )