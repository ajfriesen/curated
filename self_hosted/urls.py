from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'self-hosted'
urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:app_id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#TODO: Serving static and media files with django is not good for prod