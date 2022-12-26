# Django imports
from django.shortcuts import render

# My file imports
from .cart import Cart
# Create your views here.

def detail_cart(request):
    
    # Create object cart 
    cart = Cart(request)
    
    return render(request, "cart/cart.html", {
        'cart' : cart
    })