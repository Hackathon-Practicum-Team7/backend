from django.contrib import admin

from apps.about.models import (
    City,
    Grade,
    Profession,
    DirectionOfStudy,
    EmploymentType,
    WorkingCondition,
)


@admin.register(EmploymentType)
class EmploymentTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"


@admin.register(WorkingCondition)
class WorkingConditionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "direction")
    empty_value_display = "-пусто-"


@admin.register(DirectionOfStudy)
class DirectionOfStudyAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
