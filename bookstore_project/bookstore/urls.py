# bookstore/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Book list
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('cart/', views.view_cart, name='view_cart'),  # View cart
]