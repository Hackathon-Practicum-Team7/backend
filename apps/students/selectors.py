import uuid
from typing import List

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
    ).filter(is_looking_for_job=True)
    if skills:
        queryset = queryset.annotate(
            skill_match=Count("skills", filter=Q(skills__title__in=skills))
        ).order_by("-skill_match")
    return queryset


def get_student(id: uuid) -> Student:
    try:
        return get_all_students().get(id=id)
    except ObjectDoesNotExist:
        raise exceptions.NotFound({"details": "Объект не найден"})


def get_selected_students(students_id: list[dict]) -> QuerySet[Student]:
    ids = []
    for data in students_id:
        ids.append(uuid.UUID(data.get("id")))
    queryset = get_all_students().filter(id__in=ids)
    return queryset


def calculate_skill_match(
        student_skills: List[str], filter_skills: List[str]
) -> float:
    if not filter_skills:
        return 100
    skills = [skill for skill in student_skills if skill in filter_skills]
    total = len(skills) / len(filter_skills) * 100
    return round(total, 2)


def get_skill_match_status(total: float) -> int:
    if 75 < total <= 100:
        return 100
    elif 50 < total <= 75:
        return 75
    elif 25 < total <= 50:
        return 50
    elif 0 < total <= 25:
        return 25
    else:
        return 0
