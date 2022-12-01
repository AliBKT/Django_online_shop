from django.shortcuts import render
from django.views import generic
from .models import Product


# Create your views here.


class ListProductsView(generic.ListView):
    model = Product
    context_object_name = 'Products'
    template_name = "products/ListProduct.html"


class DetailProductView(generic.DetailView):
    model = Product
    context_object_name = 'Product'
    template_name = "products/DetailProduct.html"


