from django import template
from product.models import ProducstModel

register = template.Library()


@register.filter
def get_add_cart(request):
    cart = request.session.get('cart', [])
    products = ProducstModel.objects.filter(pk__in = cart)
    
    return products