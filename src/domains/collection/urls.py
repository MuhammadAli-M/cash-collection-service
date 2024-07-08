from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from domains.collection.infra.controllers.signup import SignupAPIView

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="signup"),
    path("signin/", TokenObtainPairView.as_view(), name="signin"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
