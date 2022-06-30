from celery import shared_task

# app = Celery('tasks', broker='pyamqp://guest@localhost:9001//')

@shared_task
def add(x, y):
    return x + y