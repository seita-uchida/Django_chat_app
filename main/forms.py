from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Talk, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

class LoginForm(AuthenticationForm):
    pass

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message",)