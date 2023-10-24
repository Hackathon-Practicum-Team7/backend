import uuid

from django.db import models
from django.utils import timezone

from apps.about.models import (
    City,
    EmploymentType,
    Grade,
    Profession,
    Skill,
    WorkingCondition,
)


class CustomMeta:
    ordering = ("-id",)


class Contact(models.Model):
    """Модель Контакты."""

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
    started_at = models.DateField()
    finished_at = models.DateField()
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
    started_at = models.DateField()
    finished_at = models.DateField()

    class Meta(CustomMeta):
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return f"{self.speciality} at {self.institute}"


class StudentSkill(models.Model):
    """Промежуточная модель скилы Студента"""

    class Score(models.TextChoices):
        """Оценка навыка"""

        BEGINNER = "beginner", "новичок"
        BASIC = "basic", "базовый уровень"
        MIDDLE = "middle", "уверенный пользователь"
        PROFESSIONAL = "professional", "профессионал"

    sudent = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="student_skill"
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name="student_skill"
    )
    score = models.CharField(
        max_length=12,
        choices=Score.choices,
        default=Score.BEGINNER,
    )


def student_resume_path(instance, filename):
    return f"student_{instance.student.id}/resumes/{filename}"


def student_avatar_path(instance, filename):
    return f"student_{instance.student.id}/avatars/{filename}"


class Student(models.Model):
    """Модель Студент."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.ForeignKey(
        Profession,
        on_delete=models.SET_NULL,
        related_name="students",
        null=True
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.SET_NULL, related_name="students", null=True
    )
    skills = models.ManyToManyField(Skill, through="StudentSkill")
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, related_name="students", null=True
    )
    started_working = models.DateField(null=True, blank=True)
    employment_types = models.ManyToManyField(EmploymentType)
    working_condition = models.ManyToManyField(WorkingCondition)
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
    def experience(self):
        if self.started_working:
            today = timezone.now()
            return today.year - self.started_working.year
        else:
            return None

    def __str__(self):
        return f"{self.name} {self.surname}"
