from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from django.urls import path
from .views import CustomRegisterView, CustomLoginView


urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", CustomLoginView.as_view(), name="rest_login"),
]
