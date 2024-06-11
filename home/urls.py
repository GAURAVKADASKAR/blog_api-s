"""
URL configuration for blog_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/',create_user.as_view()),
    path('get_blog/',getblog.as_view()),
    path('delete_blog/<id>/',delete_blog.as_view()),
    path('create_blog/',create_blog.as_view()),
    path('update_blog/<id>/',update_blog.as_view()),
]
