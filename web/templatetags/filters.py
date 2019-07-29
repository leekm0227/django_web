from django import template
from django.utils import dateparse

register = template.Library()


@register.filter(name='to_date')
def to_date(value):
    return dateparse.parse_datetime(value)


@register.filter(name='paging')
def paging(value, args):
    html = '';

    return ' [ prev ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ next ]'


register.filter('to_date', to_date)
register.filter('paging', paging)
