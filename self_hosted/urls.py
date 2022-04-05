from django.urls import path

from . import views

urlpatterns = [
    path('self-hosted', views.index, name='index'),
    path('self-hosted/<int:app_id>/', views.detail, name='detail'),
]