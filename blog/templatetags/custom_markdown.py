import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):

    return mark_safe(markdown.markdown(force_text(value), extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ]))
