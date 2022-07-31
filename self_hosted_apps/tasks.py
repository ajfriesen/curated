from celery import shared_task
import github
import asyncio
from .models import AppPage

# app = Celery('tasks', broker='pyamqp://guest@localhost:9001//')

@shared_task
def add(x, y):
    return x + y

@shared_task
def get_github_stars():

    client = github.GHClient()

    obj = client.get_repo(
        name='operating-system',
        owner='home-assistant'
        )
    
    print(obj.stargazers_count)

