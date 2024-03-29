# Django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST

# My file imports
from .cart import Cart
from .forms import AddCartProductForm
from products.models import Product


# Create your views here.

def detail_cart(request):
    # Create object cart
    cart = Cart(request=request)

    # Create form update quantity 
    for item in cart:
        item['product_update_quantity_form'] = AddCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, "cart/cart.html", {
        'cart': cart
    })


def add_to_cart(request, product_id):
    # Get object cart
    cart = Cart(request=request)

    # Get product 
    product = get_object_or_404(Product, id=product_id)

    # From received 
    form = AddCartProductForm(request.POST)

    # Form is valid do 
    if form.is_valid():
        cleaned_data = form.cleaned_data

        # Get quantity from form
        quantity = cleaned_data['quantity']

        # Get inplace from form
        inplace = cleaned_data['inplace']

        # Add product to cart
        cart.add(product=product, quantity=quantity, replaced_current_quantity=inplace)

    return redirect('product:list_products')


def remove_from_cart(request, product_id):
    # Get object cart
    cart = Cart(request=request)

    # Get product
    product = get_object_or_404(Product, id=product_id)

    # Remove form cart
    cart.remove(product=product)

    print(cart.cart)
    return redirect('cart:cart_detail')


@require_POST
def cart_clear(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _("All products successfully removed from cart"))
    else:
        messages.warning(request, _("Your cart is already empty"))

    return redirect('cart:cart_detail')
