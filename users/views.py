from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView

from .forms import SignUpForm


class SignInView(LoginView):
    template_name = "users/authForm.html"


class SignUpView(generic.CreateView):
    template_name = "users/reg.html"
    form_class = SignUpForm

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["next"] = self.request.GET.get("next", reverse("recipes"))
        return context

    def get_success_url(self):
        next_url = self.request.POST.get("next")
        return next_url


class LogoutView(LogoutView):
    pass


@method_decorator(login_required, name="dispatch")
class ChangePasswordView(PasswordChangeView):
    template_name = "users/changePassword.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("recipes")


class ResetPasswordView(PasswordResetView):
    template_name = "users/resetPassword.html"
    form_class = PasswordResetForm


class PasswordResetDone(TemplateView):
    template_name = "users/resetDone.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "users/passwordConfirm.html"
    post_reset_login = True
    success_url = reverse_lazy("recipes")
