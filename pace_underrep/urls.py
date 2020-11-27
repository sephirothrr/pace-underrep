"""pace_underrep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from datetime import datetime

import allauth
import allauth.account.forms as authforms
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic import TemplateView
from django.urls import path, include
from pace_underrep.directory import views
from pace_underrep.directory import models, forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view
        (success_url='/',
         template_name='login.html',
          authentication_form=forms.BootstrapAuthenticationForm,
         ),
         name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('', views.TemplateView.as_view(template_name='index.html'), name='home'),
    path('glossary', views.TemplateView.as_view(
        template_name='glossary.html',
        extra_context={'definitions': models.Definition.objects.all()}
        ), name='glossary'),
    path('directory', views.TemplateView.as_view(
        template_name='directory.html',
        extra_context={}
        ), name='directory'),
    path('privacy', views.TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('contact', views.TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('profile', views.TemplateView.as_view(template_name='profile.html'), name='profile'),
]
