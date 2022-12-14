from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey
import schemas, auth, github_utils


description = """
Micro API para actualizar comunidades en repo de Github.
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

@app.post("/item/", status_code=201, )
async def create_item(item: schemas.Item, api_key: APIKey = Depends(auth.get_api_key)):
    result = github_utils.sync_item(item)
    return {"result" : result }

