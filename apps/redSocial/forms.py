from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Post

class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['nombre','apellido','username', 'email', 'password1', 'password2']
        


class PostForm(forms.ModelForm):
    content = forms.CharField(label='')

    class Meta:
        model = Post
        fields = ['content']
