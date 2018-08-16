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
