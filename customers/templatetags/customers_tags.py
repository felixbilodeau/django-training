from django.template import Library
from django.utils.html import format_html


register = Library()


@register.simple_tag
def get_customer_full_name(customer):
    return format_html(
        '{} {}',
        customer.user.first_name,
        customer.user.last_name,
    )
