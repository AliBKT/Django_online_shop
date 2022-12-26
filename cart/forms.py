from django import forms

class AddCartProductForm(forms.Form):
    
    # Choice quantity in 1,...,30 range
    QUANTITY_CHOICES = [(i,str(i)) for i in range(1,20)]
    
    # Quantity field in from
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)