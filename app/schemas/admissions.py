from pydantic import BaseModel, ConfigDict
from datetime import time, date


class AdmissionsRooms(BaseModel):
    admission_no : int
    patient_no : int
    room_no : int
    admitted_time : time
    admitted_date : date
    discharge_time : time
    discharge_date : date 
    status : str


class AdmissionRoomsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    addmission_no : str
    patient_no : str
    room_no : str
    admitted_time : time
    admitted_date : date
    discharge_time : time
    discharge_date : date 
    status : str
