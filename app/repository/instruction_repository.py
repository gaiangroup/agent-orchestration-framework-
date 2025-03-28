from helpers.piDbOperations import PIDBHelper

class InstructionRepo:
    @staticmethod
    async def ingest_instruction(token: str, schemaId: str, ingest_payload: dict):
        return await PIDBHelper.ingest_instances(token, schemaId, ingest_payload, "Instructions Schema")

    @staticmethod
    async def get_instructions(token: str, schemaId: str, filter_payload: dict):
        return await PIDBHelper.filter_instances(token, schemaId, filter_payload, "Instructions Schema")

    @staticmethod
    async def update_instruction(token: str, schemaId: str, update_payload: dict):
        return await PIDBHelper.update_instances(token, schemaId, update_payload, "Instructions Schema")

    @staticmethod
    async def delete_instruction(token: str, schemaId: str, delete_payload: dict):
        return await PIDBHelper.delete_instances(token, schemaId, delete_payload, "Instructions Schema")
