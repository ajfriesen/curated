from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index


class AppPage(Page):
    """App Page model"""

    templates = "self_hosted_apps/app_page.html"

    github_link = models.URLField(blank=True)
    description = RichTextField()
    date = models.DateField("Post date")
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # Search index configuration

    # search_fields = Page.search_fields + [
    #     index.SearchField('description'),
    #     index.FilterField('date'),
    # ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('description', classname="full"),
        # InlinePanel('related_links', label="Related links"),
        FieldPanel('logo'),
        FieldPanel('github_link')
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        
    ]


    # Parent page / subpage type rules

    parent_page_types = ['AppListPage']
    subpage_types = []


# class AppPageRelatedLink(Orderable):
#     page = ParentalKey(AppPage, on_delete=models.CASCADE, related_name='related_links')
#     name = models.CharField(max_length=255)
#     url = models.URLField()

#     panels = [
#         FieldPanel('name'),
#         FieldPanel('url'),
#     ]


class AppListPage(Page):

    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['apps'] = AppPage.objects.live().public()
        return context