from django import forms
from django.db import models

from parsley.decorators import parsleyfy

from .models import Room, Comment


@parsleyfy
class NewRoomForm(forms.ModelForm):
    name = forms.CharField(min_length=3, required=True)

    class Meta:
        model = Room
        fields = ['name']
