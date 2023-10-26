import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q, QuerySet
from rest_framework import exceptions

from apps.students.models import Student


def get_all_students(skills=None) -> QuerySet[Student]:
    queryset = Student.objects.select_related(
        "profession",
        "grade",
        "city",
    ).prefetch_related(
        "skills",
        "employment_types",
        "working_condition",
    )
    if skills:
        queryset = queryset.annotate(
            skill_match=Count("skills", filter=Q(
                skills__title__in=skills)
            )
        ).order_by("-skill_match")
    return queryset


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
