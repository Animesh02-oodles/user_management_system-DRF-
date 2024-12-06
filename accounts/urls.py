from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ChangePasswordView,
    LogoutView,
    DashboardView,
    ResetPasswordRequestView,
    ResetPasswordConfirmView,
    UpdateProfileView,
    register_page  # Import the specific view for the registration page
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # API-based registration
    path('register-page/', register_page, name='register_page'),  # HTML page for registration
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Password Reset URLs
    path('reset-password-request/', ResetPasswordRequestView.as_view(), name='reset_password_request'),
    path('reset-password-confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),

    path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
]
