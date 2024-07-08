import logging
from http import HTTPStatus

from domains.collection.infra.models.user import User

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class SignupAPIView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, http_request, *args, **kwargs):
        try:
            # TODO: Add serializers to validate user input
            # TODO: Handle user db model creation by lower layers
            # TODO: Add tests
            user = User.objects.create_user(
                first_name=http_request.data["first_name"],
                last_name=http_request.data["last_name"],
                email=http_request.data["email"],
                password=http_request.data["password"],
            )

            refresh = RefreshToken.for_user(user)

            return Response({"data": {
                "user": {"id": user.id},
                "token": {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }},
                status=HTTPStatus.OK)
        except Exception as exc:
            logging.error(f"uncaught exception: {exc}")
            raise exc
