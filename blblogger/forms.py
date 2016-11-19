from django.contrib.auth.models import User
from django import forms
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('heading','post')

class UserRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['username','email','password']


class UserLogin(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['username','password']
