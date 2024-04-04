from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.


from dj_rest_auth.registration.views import (
    RegisterView,
)
from dj_rest_auth.views import LoginView
from .serializers import CustomRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        token = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "token": token,
                "user": serializer.data,
            },
            headers=headers,
        )



