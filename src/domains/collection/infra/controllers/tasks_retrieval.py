import logging
from http import HTTPStatus

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TasksRetrievalAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, http_request, *args, **kwargs):
        # usecase = CollectionUseCase()
        try:
            # response = usecase.execute().dict()
            print("requets called")
            return Response(status=HTTPStatus.OK)
        except Exception as exc:
            logging.error(f"uncaught exception: {exc}")
            raise exc
