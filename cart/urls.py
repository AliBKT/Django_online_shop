
from django.urls import path


from .views import detail_cart, add_to_cart

app_name = 'cart'

urlpatterns = [
    path('', detail_cart, name ='cart_detail'),
    path('add/<int:product_id>',add_to_cart , name='cart_add')
]
