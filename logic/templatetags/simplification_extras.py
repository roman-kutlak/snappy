import re

from django import template


register = template.Library()

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


@register.filter
def pretify(fn):
    """Convert a function name into a nicer printable version. """
    if not fn: return 'None'
    if not hasattr(fn, '__name__'): return fn
    name = fn.__name__
    s1 = first_cap_re.sub(r'\1 \2', name)
    s2 = all_cap_re.sub(r'\1 \2', s1).lower()
    s3 = s2.replace('_', ' ')
    return s3.title()

@register.filter
def fn_name(fn):
    print('fn_name: "{}"'.format(str(fn)))
    if not fn: return 'None'
    if not hasattr(fn, '__name__'): return fn
    return fn.__name__

@register.filter
def fn_doc(fn):
    if not fn: return 'None'
    if not hasattr(fn, '__doc__'): return fn
    return fn.__doc__
