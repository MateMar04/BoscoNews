from django import template

from ..models import *

register = template.Library()


@register.simple_tag
def count_news():
    return New.objects.count()


@register.simple_tag
def count_new_images(new):
    return Image.objects.filter(new=new).count()


@register.simple_tag
def get_new_images(new):
    images = Image.objects.filter(new=new)
    return images


@register.simple_tag
def define_counter():
    return 0


@register.simple_tag
def increment_counter(counter):
    return counter + 1
