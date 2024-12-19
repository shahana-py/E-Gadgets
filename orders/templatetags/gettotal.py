from django import template

register = template.Library()

@register.simple_tag(name='gettotal')
def gettotaly(cart):
    total=0
    for item in cart.added_items.all():
        total+=item.quantity*item.product.price
    return total
