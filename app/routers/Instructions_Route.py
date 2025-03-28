from fastapi import APIRouter, Header
from models.instruction_model import Instruction
from services.instructions_service import InstructionService

instruction_router = APIRouter(prefix="/instructions", tags=["Instructions"])

@instruction_router.post("/")
async def create_instruction(instruction: Instruction, authorization: str = Header(...)):
    response = await InstructionService.create_instruction_service(authorization, instruction)
    return response

@instruction_router.get("/")
async def fetch_instructions(filter_payload: dict, authorization: str = Header(...)):
    response = await InstructionService.get_instruction_service(authorization, filter_payload)
    return response

@instruction_router.put("/")
async def modify_instruction(instruction: Instruction, authorization: str = Header(...)):
    response = await InstructionService.update_instruction_service(authorization, instruction)
    return response

@instruction_router.delete("/")
async def remove_instruction(delete_payload: dict, authorization: str = Header(...)):
    response = await InstructionService.delete_instruction_service(authorization, delete_payload)
    return response
