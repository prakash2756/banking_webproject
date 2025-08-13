from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage,name='login-form'),
    path('create-account', views.createaccount,name='create-account'), 
    path('welcome-page', views.welcomepage,name='welcome-page'),        
    path('success/<str:account_number>/', views.success,name='success'),
    
]