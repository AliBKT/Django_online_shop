# Import from django library
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
# Import from files
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItems


# Create your views here.
def create_order_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) is 0:
        messages.warning(request, _('You can not proceed to checkout page because your cart is empty ! '))
        return redirect('product:list_products')

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            for item in cart:
                product = item['product_obj']
                OrderItems.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )
            cart.clear()
            messages.success(request, _('Your order has been successfully placed'))

    return render(request, 'orders/order_create.html', context={
        'form': order_form,
    })
