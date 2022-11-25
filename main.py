from fastapi import Depends, FastAPI

import schemas, auth, github_utils

from fastapi.security.api_key import APIKey
from slugify import slugify


description = """
API para actualizar comunidades en repo de Github.

[Ver código en GitHub](https://github.com/softwareguru/comunidades-api)
"""

app = FastAPI(
    title="Comunidades.dev API",
    description=description,
    version="0.1.0",
    license_info={
        "name": "MIT License",
        "url": "https://choosealicense.com/licenses/mit/",
    },
)

@app.get("/", include_in_schema=False)
async def root():
    return {"message" : "It would be nice to config your web server to show an html file instead of this."}

@app.post("/communities/", status_code=201, )
async def create_community(community: schemas.Community, api_key: APIKey = Depends(auth.get_api_key)):
    community.slug=slugify(community.title)
    result = github_utils.sync_community(community)
    return {"result" : result }
