from django.contrib import admin

from apps.students.models import Contact, Education, Job, Student, StudentSkill


class StudentSkillInline(admin.TabularInline):
    model = StudentSkill
    extra = 1


class JobInline(admin.StackedInline):
    model = Job
    extra = 1


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ("is_looking_for_job", "has_portfolio")}),
        (
            "Общая информация",
            {
                "fields": (
                    "name",
                    "surname",
                    "avatar",
                    "city",
                    "about",
                )
            },
        ),
        (
            "О работе",
            {
                "fields": (
                    "profession",
                    "grade",
                    "started_working",
                    "employment_types",
                    "working_condition",
                    "resume",
                )
            }
        ),
    ]
    inlines = (ContactInline, EducationInline, JobInline, StudentSkillInline)
    list_display = (
        "id",
        "name",
        "surname",
        "profession",
        "grade",
        "is_looking_for_job",
        "has_portfolio",
    )
    empty_value_display = "-пусто-"
