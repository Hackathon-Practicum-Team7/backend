import uuid
from http import HTTPStatus

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

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


@pytest.mark.django_db()
def test_students_view_anonymous():
    client = APIClient()
    url = reverse("student-list")
    response = client.get(url)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_student_card_view(client_client, student):
    url = reverse("student", kwargs={"id": student.id})
    response = client_client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_favorites_view(client_client):
    students_data = [
        {"id": uuid_str},
        {"id": uuid_str}
    ]
    data = {"students_id": students_data}
    url = reverse("favorite-students")
    response = client_client.post(url, data, format="json")
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_export_excel_view(client_client):
    students_data = [
        {"id": uuid_str},
        {"id": uuid_str}
    ]
    data = {"students_id": students_data}
    url = reverse("download_excel")
    response = client_client.post(url, data, format="json")
    assert response.status_code == HTTPStatus.OK
    assert response["Content-Type"].startswith("application/vnd.ms-excel")
    assert response.content


@pytest.mark.django_db
def test_download_resume_view(client_client, student_with_resume):
    url = reverse("download_resume", args=[str(student_with_resume.id)])
    response = client_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert response['Content-Disposition'] == f'attachment; filename="{student_with_resume.resume.name}"'
    assert response['Content-Type'] == 'application/pdf'
