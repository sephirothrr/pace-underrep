from datetime import datetime

from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from pace_underrep.directory import models, forms
from .models import Definition


class StaticView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def glossary(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'glossary.html',
        {
            'title': 'Glossary',
            'year': datetime.now().year,
            'definitions': Definition.objects.all()
        }
    )


def privacy(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'privacy.html',
        {
            'title': 'Privacy/FAQ',
            'message': 'Ramapriya\'s contact page.',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title': 'Contact',
            'year': datetime.now().year,
        }
    )


# def login(request):
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'login.html',
#         {
#             'title': 'Login',
#             'year': datetime.now().year,
#             'forms': forms.BootstrapAuthenticationForm
#         }
#     )

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
