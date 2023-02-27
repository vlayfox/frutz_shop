from django.urls import path
from apps.order.views import add_to_cart, cart_view,create_order,delete_from_cart_view

urlpatterns = [
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('create/', create_order, name='create_order'),
    path('delete/<int:product_id>/', delete_from_cart_view, name='delete_from_cart'),
]
