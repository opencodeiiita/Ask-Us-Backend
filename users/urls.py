from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('register/', UserRegisterView.as_view()),
]