from math import prod
from django.conf import settings
from django.http import HttpRequest
from django.conf import settings
 
def umami_analytics(request: HttpRequest):
 
    return {
        'UMAMI_KEY': settings.UMAMI_KEY,
        'UMAMI_ADDRESS': settings.UMAMI_ADDRESS,
    }
