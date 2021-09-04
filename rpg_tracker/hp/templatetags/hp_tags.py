from django import template

register = template.Library()

@register.inclusion_tag('load_skill_lists.html')
def load_skill_list(skills, first):
    return {
        'skills' : skills,
        'first' : first
    }

@register.simple_tag(name="get_quantidade_cartas_categoria")
def get_quantidade_cartas_categoria(ficha, category):
    return ficha.get_quantidade_cartas_por_categoria(category)