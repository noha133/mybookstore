from dj_rest_auth.views import LoginView
from django.urls import path
from .views import CustomRegisterView





urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),

]