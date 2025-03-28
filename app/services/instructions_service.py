from repository.instruction_repository import InstructionRepo
from models.instruction_model import Instruction
from datetime import datetime
import pytz

class InstructionService:

    instruction_schemaId = "67e64cd5329c5c378a2cace5"
    tenant_id = "f71f3593-a67a-40bc-a11a-9a44668b410d"

    @staticmethod
    def get_current_time():
        utc_now = datetime.now(tz=pytz.utc)
        ist = pytz.timezone('Asia/Kolkata')
        ist_now = utc_now.astimezone(ist)
        return ist_now.strftime('%Y-%m-%d:%H:%M:%S')

    @staticmethod
    async def create_instruction_service(token: str, instruction: Instruction):
        """Creates a new instruction entry."""
        formatted_time = InstructionService.get_current_time()
        payload = {
            "id": instruction.id,
            "instruction": instruction.instruction,
            "version": instruction.version,
            "updatedAt": formatted_time,
            "createdAt": formatted_time,
            "tenantId": InstructionService.tenant_id,
        }
        return await InstructionRepo.ingest_instruction(token, InstructionService.instruction_schemaId, payload)

    @staticmethod
    async def get_instruction_service(token: str, filter_payload: dict):
        return await InstructionRepo.get_instructions(token, InstructionService.instruction_schemaId, filter_payload)

    @staticmethod
    async def update_instruction_service(token: str, instruction: Instruction):
        formatted_time = InstructionService.get_current_time()
        payload = {
            "id": instruction.id,
            "instruction": instruction.instruction,
            "version": instruction.version,
            "updatedAt": formatted_time,
            "createdAt": formatted_time,
            "tenantId": InstructionService.tenant_id,
        }
        return await InstructionRepo.update_instruction(token, InstructionService.instruction_schemaId, payload)

    @staticmethod
    async def delete_instruction_service(token: str, delete_payload: dict):
        """Deletes an instruction."""
        return await InstructionRepo.delete_instruction(token, InstructionService.instruction_schemaId, delete_payload)
