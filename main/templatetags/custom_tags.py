from django import template

print("Registering custom tags")

register = template.Library()

@register.filter
def get_field_value(obj, field_name):
    return getattr(obj, field_name, None)