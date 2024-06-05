from django.urls import path
from .views import HomePage
from. views import About
from.views import Contact
from.views import Shop
from.views import Checkout
from.views import SingleProduct
from.views import Cart
from.views import News
from.views import SingleNews

urlpatterns = [
    path('', HomePage, name="homepage"),
    path('about-us', About, name="about"),
    path('contact', Contact, name="contact"),
    path('shop', Shop, name="shop"),
    path('check-out', Checkout, name="checkout"),
    path('single-product', SingleProduct, name="single-product"),
    path('cart', Cart, name="cart"),
    path('news', News, name="news"),
    path('single-news', SingleNews, name="single-news"),
]

