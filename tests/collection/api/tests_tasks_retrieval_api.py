from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from domains.collection.infra.models.collector import Collector
from tests.collection.infra.repos.fixtures import create_task


class TasksRetrievalAPITests(TestCase):
    tasks_endpoint = reverse("tasks")

    def signup(self, client):
        response = client.post(
            reverse("signup"),
            data={
                "first_name": "Muhammad",
                "last_name": "Ahmed",
                "email": "ma@g.com",
                "password": "xcash12345",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        return response.data["data"]

    def test_no_tasks_returns_200(self):
        # arrange
        client = APIClient()
        signup_response = self.signup(client)
        access_token = signup_response["token"]["access"]

        # act
        response = client.get(
            self.tasks_endpoint,
            headers={"Authorization": f"Bearer {access_token}"},
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data["data"]["tasks"], [])

    def test_collector_has_collected_tasks_returns_200(self):
        # arrange
        client = APIClient()
        signup_response = self.signup(client)
        access_token = signup_response["token"]["access"]
        user_id = signup_response["user"]["id"]
        collector = Collector.objects.create(
            amount=50, user_id=user_id,
        )
        task1 = create_task(collector=collector, is_collected=True)
        task2 = create_task(collector=collector, is_collected=False)
        task3 = create_task(collector=collector, is_collected=True)

        # act
        response = client.get(
            self.tasks_endpoint,
            headers={"Authorization": f"Bearer {access_token}"},
        )

        # assert
        self.assertEqual(response.status_code, HTTPStatus.OK)
        tasks = response.data["data"]["tasks"]
        self.assertEqual(len(tasks), 2)
        self.assertEqual([tasks[0]["id"], tasks[1]["id"]], [task1.id, task3.id])
