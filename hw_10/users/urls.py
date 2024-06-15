from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import LoginForm, RegisterForm

app_name = 'users'

urlpatterns =[
    path('signup/', views.RegisterView.as_view(template_name='users/register.html', form_class=RegisterForm), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout')
    ]