from django.db import models


class BaseModel(models.Model):
    """Абстрактная базовая модель с общим полем title."""

    title = models.CharField(max_length=155)

    class Meta:
        abstract = True
        ordering = ("-id",)

    def __str__(self):
        return self.title


class DirectionOfStudy(BaseModel):
    """Модель Направление обучения."""

    class Meta:
        verbose_name = "Направление обучения"
        verbose_name_plural = "Направления обучения"


class Profession(BaseModel):
    """Модель Профессия."""

    direction = models.ForeignKey(
        DirectionOfStudy,
        on_delete=models.SET_NULL,
        related_name="professions",
    )

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class Grade(BaseModel):
    """Модель Уровень навыков."""

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class Skill(BaseModel):
    """Модель Навыки."""

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class City(BaseModel):
    """Модель Город проживания."""

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class EmploymentType(BaseModel):
    """Модель Вид занятости."""

    class Meta:
        verbose_name = "Вид занятости"
        verbose_name_plural = "Вид занятости"


class WorkingCondition(BaseModel):
    """Модель Условия работы."""

    class Meta:
        verbose_name = "Условия работы"
        verbose_name_plural = "Условия работы"
