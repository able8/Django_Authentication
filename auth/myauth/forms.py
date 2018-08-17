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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': '用户名已存在！！！', 'invalid': '格式不对！'}

