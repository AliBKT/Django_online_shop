from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(blank=True, verbose_name=_("Cover"), upload_to="products/product_image")

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:detail_product', args=[self.pk])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _("Very bad")),
        ('2', _("Bad")),
        ('3', _("Normal")),
        ('4', _("Good")),
        ('5', _("Perfect"))
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('comment'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    stars = models.CharField(max_length=15, choices=PRODUCT_STARS, verbose_name='امتیاز')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product:detail_product', args=[self.product.id])
