from django.shortcuts import render

# Create your views here.

def HomePage(request):
    context = {}

    template_page='index.html'

    return render(request, template_page, context )

def About(request):
    context = {}

    template_page='about.html'

    return render(request, template_page, context )

def Contact(request):
    context = {}

    template_page='contact.html'

    return render(request, template_page, context )

def Shop(request):
    context = {}

    template_page='shop.html'

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


