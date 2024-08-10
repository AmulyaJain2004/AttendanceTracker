from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('forgotpwd/', views.forgot_password, name='forgot_password'),
]