from django.urls import path

from .views import (ChangePasswordView, LogoutView, PasswordResetConfirm,
                    PasswordResetDone, ResetPasswordView, SignInView,
                    SignUpView)

urlpatterns = [

    path("logout/", LogoutView.as_view(), name="logout"),

    path("change_password/", ChangePasswordView.as_view(),
         name="change_password"),

    path("reset_password/", ResetPasswordView.as_view(),
         name="reset_password"),

    path("password_reset_done/", PasswordResetDone.as_view(),
         name="password_reset_done"),

    path("password_reset_confirm/<uidb64>/<token>",
         PasswordResetConfirm.as_view(),
         name='password_reset_confirm'),

    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup")

]
