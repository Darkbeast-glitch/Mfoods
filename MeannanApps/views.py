from django.shortcuts import redirect, render, get_object_or_404

from .models import CartItem, HomeProducts, ProductVariation, Shop, Category, ContactUs, Cart
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def HomePage(request):
    products = HomeProducts.objects.filter(is_active=True)
    context = {
        'products': products,
    }

    template_page = 'index.html'

    return render(request, template_page, context)

    return render(request, template_page, context)

# view funtion for all shops products


def AllShop(request):
    """
    All shops takes the request and filter out the active product


    arg= request

    """
    shop = Shop.objects.filter(is_active=True)

    categories = Category.objects.annotate(product_count=Count('shop'))
    context = {
        'shop': shop,
        'categories': categories,
    }

    template_page = 'shop.html'

    return render(request, template_page, context)


# Shop View, to take care of all proudct shops

def SingleProduct(request, id):
    product = get_object_or_404(Shop, id=id)
    category = Category.objects.annotate(product_count=Count('shop'))

    context = {
        'product': product,
        'category': category,
    }

    template_page = 'shop-detail.html'

    return render(request, template_page, context)


def About(request):
    context = {}

    template_page = 'about.html'

    return render(request, template_page, context)


def Contact(request):
    contacts = ContactUs.objects.all()
    if request.method == "POST":
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact_list = ContactUs(
            name=name, email=email, phone=phone, message=message)
        contact_list.save()

        messages.success(
            request, "Heya, we received your message, we shall revert😙")

    context = {
        'contacts': contacts
    }

    template_page = 'contact.html'

    return render(request, template_page, context)


def Checkout(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    subtotal = sum(item.total_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,


    }

    template_page = 'checkout.html'
    return render(request, template_page, context)


def CartViews(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    cart_item_count = cart_items.count()
    subtotal = sum(item.total_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_item_count': cart_item_count,
        'subtotal': subtotal,


    }

    template_page = 'cart.html'

    return render(request, template_page, context)


# add to cart
@login_required
def add_to_cart(request, product_variation_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product_variation = get_object_or_404(
        ProductVariation, id=product_variation_id)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product_variant=product_variation, product=product_variation.product)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, "Yayy, we added    your product to cart😊")
    return redirect('cart')


# delete cart


def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id, cart__user=request.user)
        item.delete()
        return redirect('cart')
    except CartItem.DoesNotExist:
        return redirect('cart')


def News(request):
    context = {}

    template_page = 'news.html'

    return render(request, template_page, context)


def SingleNews(request):
    context = {}

    template_page = 'single-news.html'

    return render(request, template_page, context)


def Testimonial(request):
    context = {}

    template_page = 'testmonial.html'

    return render(request, template_page, context)


def Failed(request):
    context = {}

    template_page = '404.html'

    return render(request, template_page, context)
