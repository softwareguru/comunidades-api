from github import Github

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

def sync_community(community: schemas.Community):
    path = "content/comunidades/"+community.slug+".md"
    message = "Contents synced via API"
    temas_yaml = commas_to_yaml(community.topics_flat)
    tags_yaml = commas_to_yaml(community.tags_flat)    

    content = f"""---
title: {community.title}
ext_url: {community.url}
lastmod: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
temas:
{temas_yaml}
tags:
{tags_yaml}
---

{community.description}
    """
    result = create_or_update_file(path,message, content)
    return result

def create_or_update_file(path: str, message: str, content: str):
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

def make_list(flat_list: str):
    results = []
    if flat_list != "":
        results = [(x.strip()) for x in flat_list.split(',')]
    return results

def commas_to_yaml(flat_list: str):
    result = ""
    tmp_list = make_list(flat_list)    
    for element in tmp_list:
        result += f" - {element}\n"
    return result
