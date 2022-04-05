from django.http import HttpResponse
from django.template import loader


from .models import App

def index(request):
    latest_app_list = App.objects.order_by('-pub_date')[:5]
    template = loader.get_template('self_hosted/index.html')
    context = {
        'latest_app_list': latest_app_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, app_id):
    return HttpResponse("You're looking at app %s." % app_id)

