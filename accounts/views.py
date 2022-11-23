from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .froms import CustomUserCreationForm
# Create your views here.


class SingUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


