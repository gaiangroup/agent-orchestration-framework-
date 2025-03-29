from app.config.Env_Config import env
from app.config.Log_Config import get_logger
import httpx
log = get_logger(__name__)
class VarService:
    @staticmethod
    async def create(var):
        log.info("Variable creation start")
        var_creation_url = f"{env.AOF_SERVER_V2_URL}/api/v1/variables"

        var_payload = {
            "name": var.name,
            "value": var.value,
            "type": var.type.value
        }

        var_headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'x-request-from': 'internal'
        }
        log.debug(f"variable creation start with payload:{var_payload}")
        try:
            async with httpx.AsyncClient() as client:
                var_response = await client.post(var_creation_url, headers=var_headers, json=var_payload)
                var_response.raise_for_status() 
                #write logic here to save in pi, call here var repo class fucntion to save data to var schema
            
            return {"status": var_response.status_code, "data": var_response.json()}

        except httpx.HTTPStatusError as http_err:
            return {"error": "HTTP error occurred", "details": str(http_err)}

        except httpx.RequestError as req_err:
            return {"error": "Request failed", "details": str(req_err)}

        except Exception as err:
            return {"error": "An unexpected error occurred", "details": str(err)}
