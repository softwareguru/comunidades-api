from github import Github

from config import Settings
from functools import lru_cache
from fastapi import Depends


import models
import yaml

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()    

@lru_cache()
def get_gh():
    return Github(get_settings().github_token)

def get_repos():
    g = get_gh()
    d = {}
    for repo in g.get_user().get_repos():
        d.update( { repo.name : repo.url })
    return d

def sync_community(community: models.Community):
    path = "content/comunidades/"+community.slug+".md"
    message = "Contents synced via API"
    temas_yaml = ""
    for element in community.topics:
        temas_yaml += f" - {element}\n"
    tags_yaml = ""
    for element in community.tags:
        tags_yaml += f" - {element}\n"
    

    content = f"""---
title: {community.title}
ext_url: {community.url}
date: {community.created_on}
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
    return result["commit"]
