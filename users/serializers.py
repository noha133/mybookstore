from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers, exceptions
from django.utils.translation import gettext_lazy as _
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_account_settings
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    username = None

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and User.objects.filter(email=email).first():
            msg = _('User with this email already exists.')
            raise exceptions.ValidationError(msg)
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )
        return data

    def custom_signup(self, request, user):
        # Add custom signup logic if needed
        pass

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "username": self.validated_data.get("username", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        user.save()
        self.custom_signup(request, user)
        return user
