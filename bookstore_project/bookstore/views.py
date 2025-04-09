from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = request.session.get('cart', [])
    cart.append(book.id)
    request.session['cart'] = cart
    return redirect('book_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    return render(request, 'bookstore/cart.html', {'books': books})
