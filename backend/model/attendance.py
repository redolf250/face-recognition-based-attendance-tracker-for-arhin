
from dataclasses import dataclass

@dataclass
class Attendance():
    reference:str
    fullname:str
    contact:str
    date_stamp:str
    time_stamp:str
    attendance_status:str
    date_formated:str
    position:str

    