from django.urls import path
from . import views

app_name = 'orders'  # Add this line for namespacing

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
]
