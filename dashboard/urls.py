from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name="dashboard"

urlpatterns = [
    path('', views.index, name="index" ),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html', authentication_form = LoginForm), name='login'),
    path('protocolo/<str:protocolo>/',  views.protocol, name="protocol"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
