from django import forms

class AddCartProductForm(forms.Form):
    
    # Choice quantity in 1,...,30 range
    QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]
    
    # Quantity field in from
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    
    # Determine whether the quantity should be replaced or updated
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
    