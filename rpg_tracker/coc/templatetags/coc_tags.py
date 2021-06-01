from django import template

register = template.Library()

@register.inclusion_tag('load_caracteristics_boxes.html')
def load_caracteristics_boxes(symnonim, value):
    return {
        'symn' : symnonim,
        'base_value' : value,
        'value_div_2' : int(value / 2),
        'value_div_5' : int(value / 5)
    }