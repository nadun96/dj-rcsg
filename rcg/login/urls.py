from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('action_register', views.action_register, name='action_register'),
    path('action_login', views.action_login, name='action_login'),
]
