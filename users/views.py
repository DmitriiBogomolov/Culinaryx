from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import (PasswordChangeView, PasswordResetView,
                                       PasswordResetConfirmView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SignInView(LoginView):
    template_name = "authForm.html"


class SignUpView(generic.CreateView):
    template_name = "reg.html"
    success_url = reverse_lazy('recipes')
    form_class = SignUpForm

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


@method_decorator(login_required, name='dispatch')
class LogoutView(LogoutView):
    pass


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(PasswordChangeView):
    template_name = "changePassword.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy('recipes')


class ResetPasswordView(PasswordResetView):
    template_name = "resetPassword.html"
    form_class = PasswordResetForm


class PasswordResetDone(TemplateView):
    template_name = "resetDone.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "passwordConfirm.html"
    post_reset_login = True
    success_url = reverse_lazy('recipes')
