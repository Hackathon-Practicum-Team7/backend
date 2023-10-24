import uuid

from django.db import models
from django.utils import timezone


class CustomMeta:
    ordering = ("-id",)


class Contact(models.Model):
    """Модель Контакты."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.OneToOneField(
        "Student", on_delete=models.CASCADE, related_name="contact"
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25, unique=True)
    telegram = models.CharField(
        max_length=150, unique=True, null=True, blank=True
    )
    portfolio = models.URLField(null=True, blank=True)
    whatsapp = models.CharField(
        max_length=25, unique=True, null=True, blank=True
    )

    class Meta(CustomMeta):
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.email


class Job(models.Model):
    """Модель Работа."""

    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="jobs"
    )
    organisation = models.CharField(max_length=250)
    position = models.CharField(max_length=150)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    about = models.TextField(max_length=500)

    class Meta(CustomMeta):
        verbose_name = "Работа"
        verbose_name_plural = "Работа"

    def __str__(self):
        return self.organisation


class Education(models.Model):
    """Модель Образование."""

    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="educations"
    )
    institute = models.CharField(max_length=250)
    speciality = models.CharField(max_length=250)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta(CustomMeta):
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return f"{self.speciality} at {self.institute}"


def student_resume_path(instance, filename):
    return f"student_{instance.student.id}/resumes/{filename}"


def student_avatar_path(instance, filename):
    return f"student_{instance.student.id}/avatars/{filename}"


class Student(models.Model):
    """Модель Студент."""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.ForeignKey(
        "Profession", on_delete=models.SET_NULL, related_name="students"
    )
    grade = models.ForeignKey(
        "Grade", on_delete=models.SET_NULL, related_name="students"
    )
    skills = models.ManyToManyField("Skill")
    city = models.ForeignKey(
        "City", on_delete=models.SET_NULL, related_name="students"
    )
    started_working = models.DateField(null=True, blank=True)
    employment_types = models.ManyToManyField("EmploymentType")
    working_condition = models.ManyToManyField("WorkingCondition")
    about = models.TextField(max_length=500)
    avatar = models.ImageField(
        upload_to=student_avatar_path, null=True, blank=True
    )
    resume = models.FileField(
        upload_to=student_resume_path, null=True, blank=True
    )
    is_looking_for_job = models.BooleanField(default=True)
    has_portfolio = models.BooleanField(default=False)

    class Meta(CustomMeta):
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    @property
    def get_experience(self):
        if self.started_working:
            today = timezone.now()
            delta = today - self.started_working
            years = delta.days // 365
            months = (delta.days % 365) // 30
            return f"{years}, {months}"
        else:
            return "Нет опыта"

    def __str__(self):
        return f"{self.name} {self.surname}"
