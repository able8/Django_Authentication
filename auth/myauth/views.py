from django.shortcuts import render, redirect
import django.contrib.auth

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
