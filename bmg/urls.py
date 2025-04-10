from django.urls import path
from . import views

app_name = 'bmg'

urlpatterns = [
  path("", views.home, name="home"),
  path("login-register", views.login_register_user, name="login-register"),
  path("login-to-account", views.user_login, name="login"),
  path("logout", views.user_logout, name='logout'),
  path("about-us", views.about_us, name="about-us"),
  path("our-services", views.services, name="services"),
]
