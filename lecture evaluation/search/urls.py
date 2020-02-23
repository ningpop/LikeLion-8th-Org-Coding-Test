"""evaluation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url

from . import views

urlpatterns = [
    path('board/', views.boardLecture, name='board'),
    path('result/', views.lecture_search, name='lecture_search'),
    path('detail/<int:lecture_id>/', views.detailLecture, name='detail'),
    path('detail/<int:lecture_id>/evaluate/', views.evaluateLecture, name='evaluate'),
    path('<int:lecture_id>/delete/', views.lecture_delete, name = 'lecture_delete'),
    path('review/', views.review, name="review"),
    path('review/delete/<int:review_id>', views.review_delete, name="review_delete")
]