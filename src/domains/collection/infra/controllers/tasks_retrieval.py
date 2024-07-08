import logging
from http import HTTPStatus

from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from domains.collection.infra.usecases.tasks_retrieval import (
    TasksRetrieval,
    TasksRetrievalRequest,
)


class TasksRetrievalSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return TasksRetrievalRequest(**validated_data)


class TasksRetrievalAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TasksRetrievalSerializer

    def get(self, http_request, *args, **kwargs):
        usecase = TasksRetrieval()
        try:
            data = dict(user_id=http_request.user.id)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            usecase_request = serializer.save()
            response = usecase.execute(usecase_request).dict()
            ## TODO fix to include data in response
            return Response({"data": response}, status=HTTPStatus.OK)
        except Exception as exc:
            logging.error(f"uncaught exception: {exc}")
            raise exc
