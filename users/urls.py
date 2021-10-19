from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from users import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', obtain_auth_token, name="login")
]    