from django.contrib import admin
from .models import Order, OrderItems


# Register your models here.

class OrderItemInline(admin.StackedInline) :
    model = OrderItems
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid']
    inlines = [
        OrderItemInline
    ]


@admin.register(OrderItems)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]

