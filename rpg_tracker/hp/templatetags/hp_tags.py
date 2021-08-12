from django import template

register = template.Library()

@register.inclusion_tag('load_skill_lists.html')
def load_skill_list(skills, first):
    return {
        'skills' : skills,
        'first' : first
    }