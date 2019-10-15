from django import forms
from django.db import models

# from parsley.decorators import parsleyfy

from .models import Room, Comment


# @parsleyfy
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
