from django.shortcuts import render, redirect
import django.contrib.auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserForm, CustomEditForm
from .models import CommonUserForm


from django.contrib.auth.decorators import login_required

@login_required(login_url='myauth:login')
def user_center(request):
    # print(dir(request.user))
    content = { 'user': request.user}
    return render(request, 'myauth/user_center.html', content)

@login_required(login_url='myauth:login')
def edit_profile(request):
    if request.method == 'POST':
        editform = CustomEditForm(request.POST, instance=request.user)
        if editform.is_valid():
            editform.save()
            request.user.commonuserform.nickname = editform.cleaned_data['nickname']
            # request.user.commonuserform.birthday = editform.cleaned_data['birthday']
            request.user.commonuserform.save()
            return redirect('myauth:user_center')
    else:
        editform = CustomEditForm(instance=request.user) 

    content = {'editform': editform, 'user':request.user}
    return render(request, 'myauth/edit_profile.html', content)

@login_required(login_url='myauth:login')
def change_password(request):
    if request.method == 'POST':
        return redirect('myauth:user_center')
    else: 
        return render(request, 'myauth/change_password.html')


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
        userform = CustomUserForm(request.POST)
        if userform.is_valid():
            # 创建用户
            # user = django.contrib.auth.authenticate(request,username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'])
            user = userform.save()
            user.email = userform.cleaned_data['email']
            CommonUserForm(user=user, nickname=userform.cleaned_data['nickname'], birthday=userform.cleaned_data['birthday']).save()
            django.contrib.auth.login(request, user)
            return redirect('myauth:home')
    else:
        userform = CustomUserForm() # empty form

    content = {'register_form': userform}
    return render(request, 'myauth/register.html', content)
