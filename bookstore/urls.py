"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

router = DefaultRouter()
router.register("devices", FCMDeviceAuthorizedViewSet)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Your API Title",
#       default_version="v1",
#       description="Your API description",
#       terms_of_service="https://example.com/terms/",
#       contact=openapi.Contact(email="contact@example.com"),
#       license=openapi.License(name="MIT License"),
#    ),
#    public=True,
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", include("users.urls")),
    path("shop/", include("shop.urls")),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("api/", include(router.urls)),
    path(
            "devices/",
            FCMDeviceAuthorizedViewSet.as_view({"post": "create"}),
            name="create_fcm_device",
        ),
    ]
