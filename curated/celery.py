from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curated.settings.local')
app = Celery('curated')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
# broker_url = 'redis://localhost:6379'

# celery_broker_url = 'redis://localhost:6379/0'


# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')