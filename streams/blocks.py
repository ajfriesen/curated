"""Streamfields live in here."""

from urllib import request
from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add text')

    class Meta:
        tempalte = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"
