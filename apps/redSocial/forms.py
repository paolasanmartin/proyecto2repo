
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *

class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(label="Nombre del dueño")
    fecha_nacimiento= forms.DateField()
    apellido = forms.CharField(label="Nombre de la mascota")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['nombre','apellido', 'fecha_nacimiento', 'email', 'password1', 'password2']
        


# class TiendaForm(forms.ModelForm):
#     nombre_producto = forms.CharField()
#     descripcion = forms.CharField()
#     content = forms.CharField(label='publica aqui tu producto')


#     class Meta:
#         model = Tiendas
#         fields = ['content']

class PostForm(forms.ModelForm):
    content = forms.CharField(label='')

    class Meta:
        model = Post
        fields = ['content']


