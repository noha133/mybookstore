from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.



from dj_rest_auth.registration.views import (
    RegisterView,
)
from .serializers import CustomRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
