from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView    
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import App
from .forms import AddAppForm
from taggit.models import Tag

# Will add "tags" as context variables in tempaltes
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
    

def home(request):
    return render(request, "self_hosted/home.html")

def detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    return render(request, 'self_hosted/detail.html', {'app': app})

class AddAppView(CreateView):
    model = App
    template_name = "self_hosted/add_app.html"
    form_class = AddAppForm
    success_url = reverse_lazy('self_hosted:app_list')

class AppListView(TagMixin, ListView):
    template_name = "self_hosted/index.html"
    model = App
    paginate_by = '50'
    context_object_name = 'apps'

class TagIndexView(TagMixin, ListView):
    template_name = "self_hosted/index.html"
    model = App
    paginate_by = '50'
    context_object_name = 'apps'

    def get_queryset(self):
        return App.objects.filter(tags__slug=self.kwargs.get('slug'))

class UserLogin(LoginView):
    template_name = "self_hosted/login.html"
    next_page = '/'