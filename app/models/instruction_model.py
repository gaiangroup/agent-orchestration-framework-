from pydantic import BaseModel

class Instruction(BaseModel):
    id: str
    instruction: str
    version : str

