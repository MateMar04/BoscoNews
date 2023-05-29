from django import template

from ..models import *

register = template.Library()


@register.simple_tag
def count_news():
    return New.objects.count()


@register.simple_tag
def count_new_images(new):
    return Image.objects.filter(new=new).count()
