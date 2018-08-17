# Django_Authentication
Python Django Web开发  之登录注册  
整理自B站视频 地址：https://www.bilibili.com/video/av24753518

看视频笔记：

1. 准备
- 新建项目
```sh
django-admin startproject auth
cd auth
django-admin startapp myauth
```
- 注册 app
- 添加 urls、views
- 新建templates文件 添加html
2. 登录页面
```
app_name = 'myauth' # 添加网站名称
<a href="{% url 'myauth:home' %}">返回 主页</a>
```
3. 登录逻辑
- 迁移用户表
```sh
python manage.py migrate
```
- 创建Django admin 超级账号
```
python manage.py createsuperuser # able  ableable
```
- 登录验证
```python
if request.method == 'POST':
        user = django.contrib.auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'myauth/login.html', {'error': 'userinfo error'})
        else:
            django.contrib.auth.login(request, user)
            return redirect('myauth:home')
```
4. 退出账号
- logout
```python
def logout(request):
    django.contrib.auth.logout(request)
    return redirect('myauth:home')
```
```html
    {% if user.is_authenticated %}
        <a href="{% url 'myauth:logout' %}">退出</a>
    {% else %}
        <a href="{% url 'myauth:login' %}">登录</a>
    {% endif %}
```

5. 注册
```
from django.contrib.auth.forms import UserCreationForm

python manage.py makemigrations
python manage.py migrate

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```
6. 自定义错误信息
```python
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].error_messages = {'unique': '用户名已存在！！！', 'invalid': '格式不对！'}
```
```js
    {% if register_form.errors.username %}
    <p>用户名已存在或格式不符合要求</p>
    {{ register_form.errors.username }}
    <!-- {{ register_form.errors.username.as_jon }} -->
    {% endif %}
```
7. 个人中心
```python
@login_required(login_url='myauth:login')
def user_center(request):
    # print(dir(request.user))
    content = { 'user': request.user}
    return render(request, 'myauth/user_center.html', content)
```
8. 修改个人信息
9. 修改密码



```python
@login_required(login_url='myauth:login')
def change_password(request):
    if request.method == 'POST':
        changepwdform = PasswordChangeForm(data=request.POST, user=request.user)
        if changepwdform.is_valid():
            changepwdform.save()
            return redirect('myauth:login')
    else:
        changepwdform = PasswordChangeForm(user=request.user) 

    content = {'changepwdform': changepwdform, 'user':request.user}
    return render(request, 'myauth/change_password.html', content)
```


