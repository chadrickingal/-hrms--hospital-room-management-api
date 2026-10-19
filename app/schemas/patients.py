from pydantic import BaseModel


class RegisterPatients(BaseModel):
    patients_no : int
    patients_name : str 

class RegisterPatientsResponse(BaseModel):
    msg : str