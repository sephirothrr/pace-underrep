from datetime import datetime

from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from pace_underrep.directory import models, forms


class SignupView(View):
    pass

def signup(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'signup.html',
        {
            'title': 'Register',
            'year': datetime.now().year,
            'forms': forms.SignUpForm
        }
    )