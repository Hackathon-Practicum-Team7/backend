from django.db.models import F

from apps.about.models import City, DirectionOfStudy, Skill


def get_cities() -> list[City]:
    return City.objects.all().order_by("title")


def get_direction_of_study() -> list[DirectionOfStudy]:
    return DirectionOfStudy.objects.all().prefetch_related("professions")


def get_skills(student) -> list[Skill]:
    skills = student.skills.annotate(score=F("student_skill__score"))
    return skills


def get_all_skills() -> list[Skill]:
    return Skill.objects.all().order_by("title")
