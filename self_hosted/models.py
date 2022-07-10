from statistics import mode
from django.db import models
from django.forms import FileField
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager

# Create your models here.

def default_time():
    return timezone.now()

class App(models.Model):
    pub_date = models.DateTimeField('date published', default=default_time)
    app_name = models.CharField(max_length=250)
    description = models.TextField(default="", blank=True)
    github_url = models.URLField(default="", blank=True, max_length=300)
    slug = AutoSlugField(populate_from=['app_name'])
    svg_logo = models.FileField(upload_to='logos/', default="",blank=True)

    tags = TaggableManager(blank=True)



    def __str__(self):
        return self.app_name