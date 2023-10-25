import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from apps.students.models import Student


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Необходимо указать адрес электронной почты")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class Recruiter(AbstractBaseUser, PermissionsMixin):
    """
    Модель для Рекрутера
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(
        max_length=50,
    )
    surname = models.CharField(
        max_length=50,
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField("Активный", default=True)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Рекрутер"
        verbose_name_plural = "Рекрутеры"

    def __str__(self):
        return self.email


class Favorite(models.Model):
    recruiter = models.ForeignKey(
        Recruiter,
        on_delete=models.CASCADE,
        related_name="recruters",
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="students",
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

    def __str__(self):
        return f"{self.recruiter} : {self.student}"
