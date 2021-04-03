from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth import password_validation


User = get_user_model()


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "name", "email", "password1", "password2"]


class ChangePasswordForm(ModelForm):
    class Meta:
        model = User
        fields = ["password"]
