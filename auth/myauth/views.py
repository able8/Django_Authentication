from django.shortcuts import render, redirect
import django.contrib.auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'myauth/home.html')


def login(request):
    if request.method == 'POST':
        user = django.contrib.auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'myauth/login.html', {'error': 'userinfo error'})
        else:
            django.contrib.auth.login(request, user)
            return redirect('myauth:home')
    else:
        return render(request, 'myauth/login.html')

def logout(request):
    django.contrib.auth.logout(request)
    return redirect('myauth:home')


def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            # 创建用户
            # user = django.contrib.auth.authenticate(request,username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'])
            user = userform.save()
            django.contrib.auth.login(request, user)
            return redirect('myauth:home')
    else:
        userform = UserCreationForm() # empty form

    content = {'register_form': userform}
    return render(request, 'myauth/register.html', content)
