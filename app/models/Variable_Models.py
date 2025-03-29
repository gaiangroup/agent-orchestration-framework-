from pydantic import BaseModel
from enum import Enum

class VarEnum(str,Enum):
    runtime = "runtime"
    static = "static"


class VriableModel(BaseModel):
    name:str
    type:VarEnum
    value:str