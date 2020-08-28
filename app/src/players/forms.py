from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Player, Cube

class BasicUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['user', 'date_joined'] # With Null or default Value

class CubeForm(ModelForm):
    class Meta:
        model = Cube
        fields = '__all__'
        exclude = ['cube_id', 'users']
