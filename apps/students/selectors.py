import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from rest_framework import exceptions

from apps.students.models import Student


def get_all_students() -> QuerySet[Student]:
    return Student.objects.select_related(
        "profession",
        "grade",
        "city",
    ).prefetch_related(
        "skills",
        "employment_types",
        "working_condition",
    )


def get_student(id: uuid) -> Student:
    try:
        return get_all_students().get(id=id)
    except ObjectDoesNotExist:
        raise exceptions.NotFound({"details": "Объект не найден"})


def get_selected_students(students_id: list[dict]) -> list:
    ids = []
    for data in students_id:
        ids.append(uuid.UUID(data.get("id")))
    queryset = get_all_students().filter(id__in=ids)
    return queryset
