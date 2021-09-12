"""mindminer URL Configuration

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
from django.urls import path
from rest_framework.routers import DefaultRouter

from subject.views import SubjectViewSet
from subject.mongo_views import TweetViewSet
from news.views import NewsViewSet
from about.views import TrainingViewSet

ROUTER = DefaultRouter()
ROUTER.register(r'api/subject', SubjectViewSet)
ROUTER.register(r'api/news', NewsViewSet)
ROUTER.register(r'api/tweets', TweetViewSet, basename='api-tweet')
ROUTER.register(r'api/about/training', TrainingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + ROUTER.urls
