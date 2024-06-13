from django.shortcuts import redirect, render, get_object_or_404

from .models import BillingAddress, CartItem, HomeProducts, ProductVariation, Shop, Category, ContactUs, Cart
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
from django.core.paginator import Paginator


# Create your views here.
@csrf_exempt
def speech_recognition(request):
    if request.method == 'POST':
        try:
            query = request.POST.get('query', '')
            response_text = handle_query(query)

            # Generate speech response
            tts = gTTS(text=response_text, lang='en')
            tts.save("response.mp3")

            with open("response.mp3", "rb") as f:
                response_audio = f.read()

            response = HttpResponse(response_audio, content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename="response.mp3"'
            return response

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'speech_recognition.html')


def handle_query(query):
    query = query.lower()

    if "categories" in query:
        categories = Category.objects.values_list('category_name', flat=True)
        categories_list = ", ".join(categories)
        response_text = f"We have the following categories: {categories_list}."
    elif "products" in query:
        # Assuming you have a single shop
        shop = Shop.objects.first()  # Get the first (and probably only) shop instance

        if shop:
            # Count the number of products in the shop
            product_count = shop.products.count()

            response_text = f"There are {product_count} products in the shop."
        else:
            response_text = "The shop does not exist."
    elif "payment gateway" in query:
        # Assuming you have a setting or a model for payment gateways
        payment_gateway = "Our payment gateway is PayStack."
        response_text = payment_gateway

    elif "checkout" in query:
        response_text = "redirect_to_checkout"

    elif "who are you" in query:
        # Assuming you have a setting or a model for payment gateways
        payment_gateway = "I am a shop assistant built for Meannan Foods by Julius and the Team, Thank you.Let me know if you have any question , i will be very happy to assist you"
        response_text = payment_gateway
    elif "pepper" in query:
        pepper_text = "This pepper is a product by Meannan Foods, well packaged and outsourced, it's a powdered pepper, you can order now and get a free delivery"
        response_text = pepper_text
    else:
        response_text = "Sorry, I didn't understand your question."

    return response_text


def generate_speech(text, speed=4.0):
    from gtts import gTTS
    import os

    # Generate speech response with specified speed
    tts = gTTS(text=text, lang='en', slow=False if speed >= 1.0 else True)
    tts.save("response.mp3")

    # Read the saved MP3 file
    with open("response.mp3", "rb") as f:
        response_audio = f.read()

    # Delete the temporary MP3 file
    os.remove("response.mp3")

    return response_audio


def HomePage(request):
    products = HomeProducts.objects.filter(is_active=True)
    context = {
        'products': products,
    }

    template_page = 'index.html'

    return render(request, template_page, context)


# view funtion for all shops products

# AIVIEW


def AllShop(request):
    """
    All shops takes the request and filter out the active product


    arg= request

    """
    shop = Shop.objects.filter(is_active=True)
    # Create a Paginator
    paginator = Paginator(shop, 9)  # Show 10 products per page

    # Get the page number from the request
    page_number = request.GET.get('page')

    # Get the page of products
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.annotate(product_count=Count('shop'))
    context = {
        'shop': shop,
        'categories': categories,
        'page_obj': page_obj
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
    billing_address = BillingAddress.objects.all()
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email_address = request.POST["email_address"]
        address = request.POST["address"]
        town_city = request.POST["town"]
        phone = request.POST["phone"]

        billing_address_save = BillingAddress(first_name=first_name, last_name=last_name,
                                              emailaddress=email_address, address=address, town_city=town_city, phone=phone)
        billing_address_save.save()

    cart_items = CartItem.objects.filter(cart__user=request.user)
    subtotal = sum(item.total_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'billing_address': billing_address


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
