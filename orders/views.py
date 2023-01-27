from django.shortcuts import render


# Create your views here.
def create_order_view(request):
    return render(request, 'orders/order_create.html')
