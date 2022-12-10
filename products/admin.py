from django.contrib import admin
from .models import Product, Comment


# Register your models here.

class ProductComments(admin.StackedInline):
    model = Comment
    extra = 0
    fields = ['body', 'author', 'active', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        ProductComments
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'active', 'datetime_created']
