from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import AddAppView, index, detail

app_name = 'self-hosted'
urlpatterns = [
    path('', index, name='index'),
    path('<int:app_id>/', detail, name='detail'),
    path('create_app/', AddAppView.as_view() , name="add_app")
]