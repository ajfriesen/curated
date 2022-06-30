from django.http import Http404
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404

from .models import App
from .forms import AddAppForm
from taggit.models import Tag

def home(request):
    return render(request, "self_hosted/home.html")

def index(request):
    tag_list = Tag.objects.all
    latest_app_list = App.objects.order_by('-pub_date')[:20]
    context = {
        'latest_app_list': latest_app_list,
        'tag_list': tag_list
        }
    return render(request, "self_hosted/index.html", context )


def detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    return render(request, 'self_hosted/detail.html', {'app': app})

class AddAppView(FormView):

    template_name = "self_hosted/add_app.html"
    form_class = AddAppForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
