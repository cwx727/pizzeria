from django.urls import path, include, re_path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/',  LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/',views.logout_view),
    path('register/',views.register),

]
