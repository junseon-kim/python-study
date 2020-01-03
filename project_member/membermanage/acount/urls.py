from django.urls import path
from . import views

app_name = 'acount'

urlpatterns = [
    path('signup/', views.beforesign, name='beforesignup'),
    path('good/', views.signupwork, name='signup'),
    path('', views.loginwork, name='login'),
    path('logout/', views.logout, name='logout'),
]
