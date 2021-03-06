"""askus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from qna import views

urlpatterns = [
    path('<int:id>/', views.question_detail),
    path('new/', views.question_create),
    path('<int:id>/answer/new/', views.answer_create),
    path('<int:qid>/answer/<int:aid>/', views.answer_detail),
    path('all/',views.QuestionList.as_view()),
    path('<int:id>/answer/all/',views.AnswerList.as_view())
]
