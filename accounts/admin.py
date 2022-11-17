from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .froms import UserChangeForm, UserCreationForm
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ['username', 'email', ]
