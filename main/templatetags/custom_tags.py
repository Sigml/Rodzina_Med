from django import template

print("Registering custom tags")

register = template.Library()

@register.filter
def get_field_value(obj, field_name):
    return getattr(obj, field_name, None)


@register.filter
def is_not_null(value):
    return value is not None and value != 'Null'


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_day(doctor, day):
    return getattr(doctor, day, None)