"""HengDaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from homeApp.views import home
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),      # name='home'用于模板中进行逆向解析index.html中{% url 'home' %}
    path('aboutApp/',include('aboutApp.urls')),     # 公司简介
    path('newsApp/',include('newsApp.urls')),       # 新闻动态
    path('serviceApp/',include('serviceApp.urls')), # 服务支持
    path('productApp/',include('productApp.urls')), # 产品中心
    path('scienceApp/',include('scienceApp.urls')), # 科研基地
    path('contactApp/',include('contactApp.urls')), # 人才招聘
]
