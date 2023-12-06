from pydantic import BaseModel
from enum import Enum

class Year(str, Enum):
    year_1 = "1"
    year_2 = "2"
    year_3 = "3"
    year_4 = "4"
    year_5 = "5"

class Material(BaseModel):
    courseCode: str
    courseName: str
    courseLecturer: str
    materialName: str
    url: str
    year: Year

class Search(BaseModel):
    searchword: str
