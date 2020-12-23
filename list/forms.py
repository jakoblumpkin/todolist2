from django.forms import ModelForm
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class TaskForm(ModelForm):

    class Meta:
        model=mylist
        fields=['name','time']
        labels={"name": _('What are you doing today? '),
                "time": _('What time are you doing this? ')}


class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

