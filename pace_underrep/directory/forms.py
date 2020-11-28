"""
Definition of forms.
"""
from datetime import datetime

from django.forms import ModelForm
from django.utils import timezone

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.utils.translation import ugettext_lazy as _
from pace_underrep.directory.models import DirUser
import allauth
import allauth.account.forms as authforms


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(label=_("Email Address"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email Address'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))

    # def get_user(self):
    #     return self.request.user


class SignUpForm(ModelForm, authforms.SignupForm):
    yr = timezone.now().year
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    #                              max_length=32, help_text='First name')
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    #                             max_length=32, help_text='Last name')
    date_of_birth = forms.DateField(
        label=_('Date of Birth'),
        widget=forms.SelectDateWidget(years=[year for year in range(yr - 100, yr)]),
        initial=timezone.now()
    )

    class Meta:
        model = DirUser
        fields = ['email', 'date_of_birth']


class ProfileForm(ModelForm):
    model = DirUser

    fields = []


class ResetForm(PasswordResetForm):
    pass
