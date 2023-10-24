import uuid

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions

from apps.students.models import Student


def get_student(id: uuid) -> Student:
    try:
        obj = (
            Student.objects.select_related(
                "profession",
                "grade",
                "city",
            )
            .prefetch_related(
                "skills",
                "employment_types",
                "working_condition",
            )
            .get(id=id)
        )
    except ObjectDoesNotExist:
        raise exceptions.NotFound({"details": "Объект не найден"})
    return obj
