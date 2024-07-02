from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from app.config import settings
from app.logger import logger


api_key_header = APIKeyHeader(name="Authorization")

def authorize_request(api_key: str = Security(api_key_header)):
    """
    Authorize a request based on the provided API key.

    Args:
        api_key (str): The API key provided in the request header.

    Returns:
        dict: A dictionary containing user information if the API key is valid.

    Raises:
        HTTPException: If the API key is not valid.
    """
    logger.info("Authorization attempt with API key: %s", api_key)
    if is_valid_api_key(api_key):
        user = get_user_from_api_key(api_key)
        logger.info("Authorization successful for user: %s", user["name"])
        return user
    logger.warning("Authorization failed for API key: %s", api_key)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You're not authorized to access this resource"
    )

def is_valid_api_key(api_key: str) -> bool:
    """
    Validate the provided API key.

    Args:
        api_key (str): The API key to validate.

    Returns:
        bool: True if the API key is valid, False otherwise.
    """
    valid = api_key == settings.API_KEY
    if valid:
        logger.info("API key validation successful.")
    else:
        logger.warning("API key validation failed.")
    return valid

def get_user_from_api_key(api_key: str) -> dict:
    """
    Retrieve user information based on the provided API key.

    Args:
        api_key (str): The API key used to retrieve user information.

    Returns:
        dict: A dictionary containing user information.
    """
    logger.info("Retrieving user information for API key: %s", api_key)
    return {
        "name": "admin",
        "access": "full"
    }