from github import Github
from slugify import slugify
from config import Settings
from functools import lru_cache

import schemas
import datetime

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()    

@lru_cache()
def get_gh():
    return Github(get_settings().github_token)

def sync_item(item: schemas.Item):
    # Generate a slug from the title. "This Thing" -> "this-thing" so we can use it for filename.
    item.slug = slugify(item.title)

    # Define the path where you will put your file. If you are using Hugo, this will be content/[name of your entity]/[entity-name].md
    path = get_settings().file_dir+item.slug+".md"

    # Set message for commit.
    message = f"{item.title} synced via API on {datetime.datetime.now().strftime('%Y-%m-%d')}"

    content = make_content(item)

    result = create_or_update_file(path, message, content)

    return result

def make_content(item: schemas.Item):
    """Reads attributes from an item and arranges them into a single string that will be the contents of a text file"""

    content = "---\n"
    # We read all the attributes on the object and add them to our text 
    for k,v in item.dict().items():
        if k == "description":
            continue
        if v == "" or v == None:
            continue
        if not k.startswith("strlist_"):
            content += f'{k}: {v}\n'
        else:
            # If the key starts with strlist_ we add manually the list in yaml format
            list_title = k.replace("strlist_","")
            content += f'{list_title}: \n{strlist_to_yaml(v, list_title)}\n'

    content += f'lastmod: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
    content += "---\n\n"
    
    if item.description:
        content += f'{item.description}'
    
    return content
    

def create_or_update_file(path: str, message: str, content: str):
    """Creates or updates a text file in a GitHub repo."""
    g = get_gh()
    repo = g.get_repo(settings.repo_name)
    sha: str | None = None
    try: 
        sha = repo.get_contents(path).sha
    except:
        pass

    if sha:
        result = repo.update_file(path, message,content, sha)    
    else:
        result = repo.create_file(path, message,content)    
    return result["commit"].url

def make_list(flat_list: str, list_title: str = ""):
    """Utility function that converts a string of items separated by commas (one, two, three) into a Python list"""
    results = []
    flat_list = flat_list.replace("\n",",")
    if flat_list != "":
        if list_title == "topics":
            # Slugify topics to remove special chars.
            results = [slugify(x.strip()) for x in flat_list.split(',')]
        else:
            results = [x.strip() for x in flat_list.split(',')]
    return results

def strlist_to_yaml(flat_list: str, list_title: str = ""):
    """Utility function that converts a string of items separated by commas (one, two, three) into a string of list items in yaml format"""
    result = ""
    # First we convert our string into a Python list
    tmp_list = make_list(flat_list, list_title)
    for element in tmp_list:
        result += f" - {element}\n"
    return result
