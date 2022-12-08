# Import form django library
from django import forms

# Import form my files
from .models import Comment


# CommentFrom class for submit comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'stars', ]
