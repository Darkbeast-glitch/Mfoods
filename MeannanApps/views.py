from django.shortcuts import render,get_object_or_404
from .models import HomeProducts,Shop,Category,ContactUs
from django.db.models import Count
from django.contrib import messages
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
    """
    All shops takes the request and filter out the active product
    
    
    arg= request
    
    """
    shop = Shop.objects.filter(is_active=True)
    categories = Category.objects.annotate(product_count=Count('shop'))
    context = {
        'shop':shop,
        'categories': categories
    }

    template_page='shop.html'

    return render(request, template_page, context )


# Shop View, to take care of all proudct shops

def SingleProduct(request,id):
    product = get_object_or_404(Shop, id=id)
    category = Category.objects.annotate(product_count=Count('shop'))


    
    context = {
        'product':product,
        'category' : category,
    }

    template_page='shop-detail.html'

    return render(request, template_page, context )



def About(request):
    context = {}

    template_page='about.html'

    return render(request, template_page, context )

def Contact(request):
    contacts = ContactUs.objects.all()
    if request.method == "POST":
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        
        contact_list = ContactUs(name=name, email=email, phone=phone, message=message)
        contact_list.save()
        
        messages.success(request, "Heya, we received your message, we shall revert😙")
        
    context = {
        'contacts':contacts
    }

    template_page='contact.html'

    return render(request, template_page, context )


def Checkout(request):
    context = {}

    template_page='checkout.html'

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


def Testimonial(request):
    context = {}

    template_page='testmonial.html'

    return render(request, template_page, context )

