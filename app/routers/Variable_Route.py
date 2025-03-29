from fastapi import APIRouter, HTTPException
from app.models.Variable_Models import VriableModel
from app.config.Env_Config import env
from app.services.Veriable_Service import VarService
from app.config.Log_Config import get_logger

log = get_logger(__name__)

variableRouter = APIRouter(prefix="/variable")

@variableRouter.post("")
async def Create_Var(var:VriableModel):
    log.info("Request is in create var route")
    log.debug(f"Request came in var route with this payload:{var}")
    try:
        return await VarService.create(var)
    except Exception as e:
        log.error(f"Error in Create_Var: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
        

    
    