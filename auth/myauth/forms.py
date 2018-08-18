from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
   captcha = CaptchaField()

class CustomEditForm(UserChangeForm):
    nickname = forms.CharField(required=False, max_length=50)
    birthday = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'nickname', 'birthday') # 指定普通用户可以修改的字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': '用户名已存在！！！', 'invalid': '格式不对！'}


class CustomUserForm(UserCreationForm):
    nickname = forms.CharField(required=False, max_length=50)
    birthday = forms.DateField(required=False)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'email', 'nickname', 'birthday')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': '用户名已存在！！！', 'invalid': '格式不对！'}

