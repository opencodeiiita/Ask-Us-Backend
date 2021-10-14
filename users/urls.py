from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
]