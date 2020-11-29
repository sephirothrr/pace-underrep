"""pace_underrep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import allauth.account.views as authviews
import allauth.account.forms as authforms
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView, DetailView
from pace_underrep.directory import views, models, forms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', authviews.LoginView.as_view
        (success_url='/',
         template_name='login.html',
         form_class=authforms.LoginForm,
         ),
         name='login'),
    path('accounts/signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('glossary', TemplateView.as_view(
        template_name='glossary.html',
        extra_context={'definitions': models.Definition.objects.all()}
        ), name='glossary'),
    path('directory', TemplateView.as_view(
        template_name='directory.html',
        extra_context={}
        ), name='directory'),
    path('privacy', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('profile', login_required(DetailView.as_view(model=models.DirUser, template_name='profile.html')), name='profile'),
]