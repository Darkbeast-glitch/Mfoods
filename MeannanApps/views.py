from django.shortcuts import render
from .models import HomeProducts,Shop
# Create your views here.

def HomePage(request):
    products = HomeProducts.objects.filter(is_active=True)
    context = {
        'products':products,
    }

    template_page='index.html'

    return render(request, template_page, context )

    return render(request, template_page, context )

# view funtion for all shops products
def AllShop(request):
    shop = Shop.objects.filter(is_active=True)
    context = {
        'shop':shop
    }

    template_page='shop.html'

    return render(request, template_page, context )


def About(request):
    context = {}

    template_page='about.html'

    return render(request, template_page, context )

def Contact(request):
    context = {}

    template_page='contact.html'

    return render(request, template_page, context )


def Checkout(request):
    context = {}

    template_page='checkout.html'

    return render(request, template_page, context )

def SingleProduct(request):
    context = {}

    template_page='single-product.html'

    return render(request, template_page, context )

def Cart(request):
    context = {}

    template_page='cart.html'

    return render(request, template_page, context )

def News(request):
    context = {}

    template_page='news.html'

    return render(request, template_page, context )


def SingleNews(request):
    context = {}

    template_page='single-news.html'

    return render(request, template_page, context )


