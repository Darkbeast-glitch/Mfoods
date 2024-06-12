from .models import CartItem


def cart_item_count(request):
    if request.user.is_authenticated:
        count = CartItem.objects.filter(cart__user=request.user).count()
    else:
        count = 0
    return {'cart_item_count': count}
