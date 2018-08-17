from django.urls import path, include
from . import views

app_name = 'myauth'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user_center/', views.user_center, name='user_center'),
    path('user_center/edit_profile', views.edit_profile, name='edit_profile'),
    path('user_center/change_password', views.change_password, name='change_password'),
]
