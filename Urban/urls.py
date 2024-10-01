"""
URL configuration for Urban project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.contrib import admin
# from django.urls import path
# from task2.views import blog

# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', menu_page),
    # path('shop/', shop_page),
    # path('bin/', bin_page),
    # path('html/', sign_up_by_html),
    # path('django/', sign_up_by_django)
    #path('blog', blog),
#]
from django.contrib import admin
from django.urls import path
from task1_.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('shop/', shop_page),
    path('bin/', bin_page),
    path('game/', collect_of_games),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),
    path('html_sign_up/', sign_up_by_html, name='html_sign_up'),
]