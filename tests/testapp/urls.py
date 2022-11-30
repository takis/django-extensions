# -*- coding: utf-8 -*-
"""
URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.urls import path

login_view = auth_views.LoginView.as_view() if hasattr(auth_views, 'LoginView') else auth_views.login
logout_view = auth_views.LogoutView.as_view() if hasattr(auth_views, 'LogoutView') else auth_views.logout


def example_view_no_decorator(request):
    return HttpResponse()


@login_required
def example_view_decorator_login_required(request):
    return HttpResponse()


@permission_required("loading.view_list")
def example_view_decorator_permission_required(request):
    return HttpResponse()


@staff_member_required
def example_view_decorator_staff(request):
    return HttpResponse()


urlpatterns = [
    path('login/', login_view, {'template_name': 'login.html'}, name="login"),
    path('logout/', logout_view, name="logout"),
    path('admin/', admin.site.urls),
    path("example_no_decorator", example_view_no_decorator),
    path("example_login_required", example_view_decorator_login_required),
    path("example_permission_required", example_view_decorator_permission_required),
    path("example_staff", example_view_decorator_staff),
]
