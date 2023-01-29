# Import from django library
from django import forms

# Import my files
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes', ]
        widgets = {
            'order_notes': forms.Textarea(attrs={
                'rows': 3
            }),
            'address': forms.Textarea(attrs={
                'rows': 2
            })
        }
