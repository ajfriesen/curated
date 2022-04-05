from django.urls import path

from . import views

app_name = 'self-hosted'
urlpatterns = [
    path('self-hosted', views.index, name='index'),
    path('self-hosted/<int:app_id>/', views.detail, name='detail'),
]