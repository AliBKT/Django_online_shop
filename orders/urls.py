from django.urls import path

from .views import create_order_view

app_name = 'order'

urlpatterns = [
    path('create/', create_order_view, name="create_order"),
]
