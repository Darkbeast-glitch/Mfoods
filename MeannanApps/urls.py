from django.urls import path
from .views import (
    HomePage,
    About,
    Contact,
    AllShop,
    Checkout,
    SingleProduct,
    CartViews,
    News,
    SingleNews,
    Testimonial,
    Failed,
    add_to_cart,
    remove_from_cart
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomePage, name="homepage"),
    path("about-us", About, name="about"),
    path("contact", Contact, name="contact"),
    path("shop", AllShop, name="shop"),
    path("checkout", Checkout, name="checkout"),
    path("single-product/<int:id>/", SingleProduct, name="single-product"),
    path("cart", CartViews, name="cart"),
    path("news", News, name="news"),
    path("single-news", SingleNews, name="single-news"),
    path("testimonial", Testimonial, name="testimonial"),
    path("404", Failed, name="404"),
    path('add_to_cart/<int:product_variation_id>/',
         add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
