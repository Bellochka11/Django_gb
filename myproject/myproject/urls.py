"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from myapp3.views import index

urlpatterns = [
    path('admin/', admin.site.urls), #http://127.0.0.1:8000/admin/
    path('prefix/', include('myapp.urls')), #http://127.0.0.1:8000/prefix/about/ после порта пишем prefix т.к. написали это
    path('les3/', include('myapp3.urls')), #управление передаем в myapp3 и проверить продолжение адреса там
    path('', index), #базовый адрес сайта
    path('les4/', include('myapp4.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),#отладка
    path('les6/', include('myapp6.urls')),

]