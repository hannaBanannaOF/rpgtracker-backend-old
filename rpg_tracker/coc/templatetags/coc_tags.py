from django import template

register = template.Library()

@register.inclusion_tag('load_caracteristics_boxes.html')
def load_caracteristics_boxes(symnonim, value, show_divs, base_value_pre="", base_value_app="", full_cols=False):
    return {
        'symn' : symnonim,
        'base_value' : value,
        'base_value_pre' : base_value_pre,
        'base_value_app' : base_value_app,
        'value_div_2' : int(value / 2) if show_divs else 0,
        'value_div_5' : int(value / 5) if show_divs else 0,
        'show_divs' : show_divs,
        'full_cols' : full_cols
    }