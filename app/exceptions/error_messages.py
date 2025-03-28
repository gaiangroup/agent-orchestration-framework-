from fastapi import status
from app.models.error import Error

class ErrorMessages:

    """HTTP_400_BAD_REQUEST"""

    AGENT_NAME_NULL = Error(
        http_status=status.HTTP_400_BAD_REQUEST,
        error_code=400000,
        message="Agent name shouldn't be null ",
        root_message="Provide a valid name for to create the agent"
    )

    """HTTP_409_CONFLICT"""

    AGENT_NAME_EXIST = Error(
        http_status=status.HTTP_409_CONFLICT,
        error_code=409000,
        message="Agent exist with same name",
        root_message="Ensure to provide unique names for the agents"
    )

    """HTTP_404_NOT_FOUND"""''


    AGENT_NAME_EXIST = Error(
        http_status=status.HTTP_404_NOT_FOUND,
        error_code=409000,
        message="Agent not found with ID provided",
        root_message="Provided valid agent ID"
    )

    """HTTP_401_UNAUTHORIZED"""

    UNAUTHORIZED = Error(
        http_status=status.HTTP_401_UNAUTHORIZED,
        error_code=409000,
        message="Tenant is unauthorized to access the artifact",
        root_message="Request the access from artifact owner"
    )

