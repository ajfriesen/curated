from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField


# Create your models here.

def default_time():
    return timezone.now()

class App(models.Model):
    pub_date = models.DateTimeField('date published', default=default_time)
    app_name = models.CharField(max_length=250)
    description = models.TextField(default="")
    slug = AutoSlugField(populate_from=['app_name'])


    def __str__(self):
        return self.app_name