from config import Settings
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN

from functools import lru_cache

@lru_cache()
def get_settings():
    return Settings()

api_key_header_raw = APIKeyHeader(name="access_token", auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header_raw), settings: Settings = Depends(get_settings)):
    if api_key_header == settings.api_key:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail=f"Could not validate API KEY. Got raw {api_key_header_raw} and processed {api_key_header}. Expected {settings.api_key}"
        )
