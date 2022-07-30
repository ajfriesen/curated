from django.db import models

from wagtail.core.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


# Create your models here.

class HomePage(Page):
    """Home page model."""

    templates = "home/home_page.html"

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]