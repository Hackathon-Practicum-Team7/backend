import pytest
from rest_framework.reverse import reverse

from apps.api.v1.serializers.auxiliary import (DirectionOfSudySerialiser,
                                               InfoOutputSerializer)


class TestStudentCardSerializer:
    @pytest.mark.django_db(transaction=True)
    def test_validate_fields(self, client_client, student):
        url = reverse("student", kwargs={"id": student.id})
        response = client_client.get(url)
        data = response.data

        expected_fields = [
            "id",
            "name",
            "surname",
            "city",
            "profession",
            "grade",
            "employment_types",
            "working_condition",
            "contact",
            "avatar",
            "experience",
            "jobs",
            "educations",
            "about",
            "skills",
            "resume",
            "is_favorited"
        ]

        assert list(data) == expected_fields


class TestInfoOutputSerializer:
    @pytest.mark.django_db(transaction=True)
    def test_serializer_output(self):
        data = {
            "id": 1,
            "title": "Example City",
        }

        serializer = InfoOutputSerializer(instance=data)
        serialized_data = serializer.data
        assert serialized_data["id"] == data["id"]
        assert serialized_data["title"] == data["title"]


class TestDirectionOfSudySerialiser:
    @pytest.mark.django_db(transaction=True)
    def test_serializer_output(self):
        data = {
            "id": 1,
            "title": "Example Direction",
            "professions": [
                {"id": 1, "title": "Profession 1"},
                {"id": 2, "title": "Profession 2"}
            ]
        }

        serializer = DirectionOfSudySerialiser(instance=data)
        serialized_data = serializer.data
        assert serialized_data["id"] == data["id"]
        assert serialized_data["title"] == data["title"]
        professions = serialized_data["professions"]
        assert len(professions) == len(data["professions"])
        for serialized_profession, original_profession in zip(professions, data["professions"]):
            assert serialized_profession["id"] == original_profession["id"]
            assert serialized_profession["title"] == original_profession["title"]
