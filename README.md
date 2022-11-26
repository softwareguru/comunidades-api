# API for comunidades.dev

Very simple API used for creating/updating files in a GitHub repo.

Built on top of FastAPI. Can be deployed as a Python app on a regular server, or as an image that runs in a serverless environment (ie Google Cloud Run).

Instructions:
 1. Clone the repo
 2. (Optional) Create a virtual environment or whatever you use to manage python environments.
 3. Install requirements `pip install -r requirements.txt`
 4. Change the code so that it matches the information/fields that you want to capture and write. You want to modify `schemas.py` and `github_utils.py` 
 5. Set the required environment variables (check config.py) for github token, github repo name, and an api key.
 6. Deploy to your preferred environment.

## Security
By default, POST calls expect a request header called `access-token` whose value needs to match the environment variable `api_key`. You can remove this by
removing  `api_key: APIKey = Depends(auth.get_api_key)` from the definition of `create_community` function in main.py. Or if you want to do something more sophisticated, 
change the implementation in auth.py.
