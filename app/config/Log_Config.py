import logging
import sys
import os
from datetime import datetime
from uvicorn.logging import DefaultFormatter 

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
console_formatter = DefaultFormatter(fmt="%(levelprefix)s %(message)s") 
console_handler.setFormatter(console_formatter)

log_file_path = os.path.join(LOG_DIR, f"app_{datetime.now().strftime('%Y-%m-%d')}.log")
file_handler = logging.FileHandler(log_file_path)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - Message: %(message)s") 
file_handler.setFormatter(file_formatter)


logger.handlers.clear()
logger.addHandler(console_handler) 
logger.addHandler(file_handler)  

def get_logger(name: str):
    return logger 
