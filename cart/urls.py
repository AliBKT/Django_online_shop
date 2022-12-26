
from django.urls import path


from .views import detail_cart

urlpatterns = [
    path('', detail_cart, name ='cart_detail'),
]
