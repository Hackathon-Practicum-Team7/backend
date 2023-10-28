import uuid
from http import HTTPStatus

import pytest

from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from tests.conftest import client_client, student

uuid_str = str(uuid.uuid4())


@pytest.mark.django_db()
def test_city_view():
    client = APIClient()
    url = reverse("cities")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db()
def test_professions_view():
    client = APIClient()
    url = reverse("professions")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db()
def test_skills_view():
    client = APIClient()
    url = reverse("skills")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db()
def test_students_view(client_client):
    url = reverse("student-list")
    response = client_client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_student_card_view(client_client, student):
    url = reverse("student", kwargs={"id": student.id})
    response = client_client.get(url)
    assert response.status_code == HTTPStatus.OK


# @pytest.mark.django_db
# def test_favorites_view(client_client):
#     students_data = [
#         {"id": str(uuid.uuid4())},
#         {"id": str(uuid.uuid4())}
#     ]
#     data = {"students": students_data}
#     url = reverse("favorite-students")
#     response = client_client.post(url, data, format="json")
#     assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_export_excel_view(client_client):
    url = reverse("download_excel")
    students_data = [
        {"id": str(uuid.uuid4())},
        {"id": str(uuid.uuid4())}
    ]
    data = {"students": students_data}
    response = client_client.post(url, data, format="json")
    assert response.status_code == HTTPStatus.OK
    assert response["Content-Type"].startswith("application/vnd.ms-excel")
    assert response.content


# @pytest.mark.django_db
# def test_download_resume_view(client_client):
#     url = reverse("download_resume", kwargs={"id": uuid_str})
#     response = client_client.get(url)
#     assert response.status_code == HTTPStatus.OK
#     assert response.content



