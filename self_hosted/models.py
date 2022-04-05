from django.db import models
from django.utils import timezone


# Create your models here.

def default_time():
    return timezone.now()

class App(models.Model):
    pub_date = models.DateTimeField('date published', default=default_time)
    app_name = models.CharField(max_length=250)

    def __str__(self):
        return self.app_name