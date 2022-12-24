# Import from django library

from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

# Import from my files
from .forms import CommentForm
from .models import Product, Comment
from .comment.filter import check_comment

# Create your views here.


class ListProductsView(generic.ListView):
    model = Product
    context_object_name = 'Products'
    template_name = "products/ListProduct.html"


class DetailProductView(generic.DetailView):
    model = Product
    context_object_name = 'Product'
    template_name = "products/DetailProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        object_to_db = form.save(commit=False)
        object_to_db.author = self.request.user
        object_to_db.active = check_comment(object_to_db.body)

        if object_to_db.active == False :
            messages.error(self.request, _('Your comment have inappropriate words'))
        else :
            messages.success(self.request, _('Your comment has been registered successfully'))
        
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)

        object_to_db.product = product

        return super().form_valid(form=form)
