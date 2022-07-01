from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import AddAppView, home, detail, TagIndexView, AppListView

app_name = 'self-hosted'
urlpatterns = [
    path('', home, name='home'),
    path('self-hosted', AppListView.as_view(), name='index'),
    path('<int:app_id>/', detail, name='detail'),
    path('create_app/', AddAppView.as_view() , name="add_app"),
    path('self-hosted/tags/<slug>', TagIndexView.as_view(), name='tagged'),

]