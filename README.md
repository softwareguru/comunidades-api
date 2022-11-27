# API for comunidades.dev

Very simple API used for creating/updating files in a GitHub repo.

Built on top of FastAPI. Can be deployed as a Python app on a regular server, or as an image that runs in a serverless environment (ie Google Cloud Run).

Instructions:
 1. Clone the repo
 2. (Optional) Create a virtual environment or whatever you use to manage python environments.
 3. Install requirements `pip install -r requirements.txt`
 4. Change the code so that it matches the information/fields that you want to capture and write. You want to modify `schemas.py` and `github_utils.py`. 
 5. Deploy to your preferred environment. For running in Google Cloud run simply configure your gcloud client and do `gcloud run deploy`.
 6. Set the required environment variables (see below).
 
## Environment variables
Set the following environment variables:
 * API_KEY - Set this same value as a request header named `access-token` in POST calls. Otherwise, you will get a forbidden status code.
 * REPO_NAME - The name of your github repo, in format "owner/repo_name".
 * GITHUB_TOKEN - A token with permission to write to your GitHub repo. If you don't know how to create one, [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](read this).
  * FILE_DIR - The path inside your repo where you want files to be generated. If you are using Hugo, it will be `content/something/` where something is the name of the entity you are creating.


## Security
By default, POST calls expect a request header called `access-token` whose value needs to match the environment variable `api_key`. You can remove this by
removing  `api_key: APIKey = Depends(auth.get_api_key)` from the definition of `create_community` function in main.py. Or if you want to do something more sophisticated, 
change the implementation in auth.py.
