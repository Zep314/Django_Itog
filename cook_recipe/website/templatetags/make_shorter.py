import textwrap
from django import template

register = template.Library()


@register.filter()
def make_shorter(filtering_str, filtering_width=100):
#def make_shorter(filtering_str):
    return textwrap.shorten(filtering_str, width=filtering_width, placeholder="...")
#    return filtering_str.lower()
