from datetime import datetime

from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext, gettext_lazy as _
from pace_underrep.directory import models, forms


class SignupView(CreateView):
    form_class = forms.SignUpForm
    success_url = _('/accounts/login')
    template_name = 'signup.html'
