from django.urls import path
from . import views

app_name = 'acount'

urlpatterns = [
    path('signup/', views.signupwork, name='signup'),
    path('', views.loginwork, name='login'),
    path('signup/success/', views.loginwork, name='sglogin'),
    path('logout/', views.logout, name='logout'),
]
