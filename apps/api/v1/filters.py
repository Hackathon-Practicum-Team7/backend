from django_filters.rest_framework import FilterSet, filters

from apps.about.models import (City, EmploymentType, Grade, Profession, Skill,
                               WorkingCondition)
from apps.students.models import Student


class StudentFilter(FilterSet):
    """Фильтры для студентов."""

    profession = filters.ModelMultipleChoiceFilter(
        field_name="profession__title",
        to_field_name="title",
        queryset=Profession.objects.all(),
    )

    skills = filters.ModelMultipleChoiceFilter(
        field_name="skills__title",
        to_field_name="title",
        queryset=Skill.objects.all(),
        # conjoined=True - условие для AND фильтрации
    )

    city = filters.ModelMultipleChoiceFilter(
        field_name="city__title",
        to_field_name="title",
        queryset=City.objects.all(),
    )

    employment_types = filters.ModelMultipleChoiceFilter(
        field_name="employment_types__title",
        to_field_name="title",
        queryset=EmploymentType.objects.all(),
    )

    working_condition = filters.ModelMultipleChoiceFilter(
        field_name="working_condition__title",
        to_field_name="title",
        queryset=WorkingCondition.objects.all(),
    )

    has_portfolio = filters.BooleanFilter(
        field_name="has_portfolio",
        lookup_expr="exact",
    )

    grade = filters.ModelMultipleChoiceFilter(
        field_name="grade__title",
        to_field_name="title",
        queryset=Grade.objects.all(),
    )

    class Meta:
        model = Student
        fields = (
            "profession",
            "skills",
            "city",
            "employment_types",
            "working_condition",
            "has_portfolio",
            "grade",
        )
