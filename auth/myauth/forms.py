from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    昵称 = forms.CharField(required=False, max_length=50)
    生日 = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'email', '昵称', '生日')
        # fields = ('username', 'password1', 'email', 'nikename', 'birthday')