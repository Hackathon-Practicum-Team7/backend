from django.db import models


class CustomMeta:
    ordering = ('-id',)


class DirectionOfStudy(models.Model):
    """Модель Направление обучения."""
    title = models.CharField(max_length=155)

    class Meta(CustomMeta):
        verbose_name = 'Направление обучения'
        verbose_name_plural = 'Направления обучения'

    def __str__(self):
        return self.title


class Profession(models.Model):
    """Модель Профессия."""
    title = models.CharField(max_length=155)
    direction = models.ForeignKey(
        'DirectionOfStudy',
        on_delete=models.SET_NULL,
        related_name='professions',
    )

    class Meta(CustomMeta):
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title


class Grade(models.Model):
    """Модель Уровень навыков."""
    title = models.CharField(max_length=155)

    class Meta(CustomMeta):
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Модель Навыки."""
    title = models.CharField(max_length=155)

    class Meta(CustomMeta):
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title


class City(models.Model):
    """Модель Город проживания."""
    title = models.CharField(max_length=155)

    class Meta(CustomMeta):
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title


class EmploymentType(models.Model):
    """Модель Вид занятости."""
    title = models.CharField(max_length=155)

    class Meta(CustomMeta):
        verbose_name = 'Вид занятости'
        verbose_name_plural = 'Вид занятости'

    def __str__(self):
        return self.title


class WorkingCondition(models.Model):
    """Модель Условия работы."""
    title = models.CharField(max_length=155)

    class Meta(CustomMeta):
        verbose_name = 'Условия работы'
        verbose_name_plural = 'Условия работы'

    def __str__(self):
        return self.title
