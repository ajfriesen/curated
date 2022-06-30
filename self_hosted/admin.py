from django.contrib import admin

# Register your models here.

from .models import App

@admin.register(App)
class App(admin.ModelAdmin):
    list_display= ['app_name', 'get_tags']

    def get_tags(self, object):
        return ", ".join (obj for obj in object.tags.names())
