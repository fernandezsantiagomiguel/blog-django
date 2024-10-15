from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='is_colab')
def is_colab(user):
    return user.groups.filter(name='colaborador').exists()