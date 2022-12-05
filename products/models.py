from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_product', args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', "Very bad"),
        ('2', "Bad"),
        ('3', "Normal"),
        ('4', "Good"),
        ('5', "Perfect")
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    stars = models.CharField(max_length=15, choices=PRODUCT_STARS)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
