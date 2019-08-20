from django import template
from django.utils import dateparse
from django.utils.safestring import mark_safe
import math

register = template.Library()


@register.filter(name='to_date')
def to_date(value):
    return dateparse.parse_datetime(value)


@register.simple_tag
def paging(request, total):
    row_count = 10
    paging_size = 5
    page = int(request.GET.get('page', 1))
    last_page = math.ceil(total / row_count)
    start_page = math.floor((page - 1) / paging_size) * paging_size + 1
    end_page = (start_page + paging_size) if last_page > (start_page + paging_size - 1) else last_page
    pre_page = page - paging_size if page - paging_size > 1 else 1
    nxt_page = page + paging_size if page + paging_size < last_page else last_page
    html = '<a href="?page={page}">prev</a>'.format(page=pre_page)

    for i in range(start_page, end_page + 1):
        html += '<a href="?page={page}" class="{on}">{page}</a>'.format(page=i, on="on" if page == i else "")

    html += '<a href="?page={page}">next</a>'.format(page=nxt_page)

    return mark_safe(html)


# register.filter('to_date', to_date)
# register.filter('paging', paging)
