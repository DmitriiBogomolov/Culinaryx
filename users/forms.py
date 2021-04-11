from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       ValidationError)
from django import forms
from .validators import validate_name

User = get_user_model()


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=40,
        required=True,
        validators=[
            validate_name
        ]
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_full_name(self):
        data = self.cleaned_data['full_name']
        return data.title()

    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        first_name, last_name = self.cleaned_data['full_name'].split(' ')
        instance.first_name = first_name
        instance.last_name = last_name
        if commit:
            instance.save()
        return instance


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password"]
