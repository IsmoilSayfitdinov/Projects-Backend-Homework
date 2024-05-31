from django.urls import path
from .views import RegisterView,  LoginView, verfiy_email_code_check

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email/verfiy/', verfiy_email_code_check, name="email")
]                                   