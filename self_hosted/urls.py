from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'self-hosted'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:app_id>/', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Static files will only be served in DEBUG mode per default
# https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development