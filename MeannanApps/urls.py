from django.urls import path
from .views import HomePage,About,Contact,AllShop,Checkout,SingleProduct,Cart,News,SingleNews

urlpatterns = [
    path('', HomePage, name="homepage"),
    path('about-us', About, name="about"),
    path('contact', Contact, name="contact"),
    path('shop', AllShop, name="shop"),
    path('check-out', Checkout, name="checkout"),
    path('single-product', SingleProduct, name="single-product"),
    path('cart', Cart, name="cart"),
    path('news', News, name="news"),
    path('single-news', SingleNews, name="single-news"),
]

