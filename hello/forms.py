from django import forms
from django.db import models
from django.db.models import fields
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','desc')