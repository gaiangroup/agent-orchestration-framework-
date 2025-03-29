import requests
from fastapi import HTTPException

class PIDBHelper:

    BASE_URL = "https://ig.gov-cloud.ai/pi-entity-instances-service/v2.0"

    @staticmethod
    async def ingest_instances(token: str, schemaId: str, payload: dict, schemaName="null"):
        url = f"{PIDBHelper.BASE_URL}/schemas/{schemaId}/instances"
        headers = {"Content-Type": "application/json", "Authorization": token}
        payload_for_post = {"data": [payload]}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload_for_post)
        if response.status_code not in [200, 204]:
            raise HTTPException(status_code=500, detail=f"Failed to ingest data into {schemaName}: {response.json()}")
        return response.json()

    @staticmethod
    async def filter_instances(token: str, schemaId: str, payload: dict, schemaName="null"):
        url = f"{PIDBHelper.BASE_URL}/schemas/{schemaId}/instances/list"
        headers = {"Content-Type": "application/json", "Authorization": token}
        payload_to_fetch = {"dbType": "MONGO", "ownedOnly": "true", "filter": payload}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload_to_fetch)
        if response.status_code not in [200, 204]:
            raise HTTPException(status_code=500, detail=f"Failed to retrieve data from {schemaName}: {response.json()}")
        return response.json()

    @staticmethod
    async def update_instances(token: str, schemaId: str, payload: list, schemaName="null"):
        url = f"{PIDBHelper.BASE_URL}/schemas/{schemaId}/instances"
        headers = {"Content-Type": "application/json", "Authorization": token}
        payload_to_update = {"primarykeyEnable": "true", "data": payload}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload_to_update)
        if response.status_code not in [200, 204]:
            raise HTTPException(status_code=500, detail=f"Failed to update data in {schemaName}: {response.json()}")
        return response.json()

    @staticmethod
    async def delete_instances(token: str, schemaId: str, payload: dict, schemaName="null"):
        url = f"{PIDBHelper.BASE_URL}/schemas/{schemaId}/instances?confirmDelete=true"
        headers = {"Content-Type": "application/json", "Authorization": token}
        payload_to_delete = {"dbType": "TIDB", "filter": payload}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload_to_delete)
        if response.status_code not in [200, 204]:
            raise HTTPException(status_code=500, detail=f"Failed to delete data from {schemaName}: {response.json()}")
        return response.json()
