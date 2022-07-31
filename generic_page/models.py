from tabnanny import verbose
from wagtail.models import Page

# Create your models here.

class GenericPage(Page):

    templates = "generic_page/generic_page.html"

    class Meta:
        verbose_name = "Generic page"
        verbose_name_plural = "Generic pages"