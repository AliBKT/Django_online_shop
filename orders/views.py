# Import from django library
from django.shortcuts import render
# Import from files
from .forms import OrderForm


# Create your views here.
def create_order_view(request):
    return render(request, 'orders/order_create.html', context={
        'form': OrderForm(),
    })
