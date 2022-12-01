from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProductsView.as_view(), name='list_products'),
    path('<int:pk>/', views.DetailProductView.as_view(), name="detail_product"),

]
