from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage,name='login-form'),
    path('create-account', views.createaccount,name='create-account'), 
    path('welcome-page', views.welcomepage,name='welcome-page'),        
    path('success', views.success,name='success'),
    path('AddTransaction', views.add_transaction,name='AddTransaction'),
    path('logout', views.logout_view,name='logout'),
]