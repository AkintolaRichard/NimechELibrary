from pydantic import BaseModel

class Material(BaseModel):
    courseCode: str
    courseName: str
    courseLecturer: str
    materialName: str
    url: str

class Search(BaseModel):
    searchword: str
