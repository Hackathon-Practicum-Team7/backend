# Generated by Django 4.1 on 2023-10-24 07:20

import apps.students.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("started_working", models.DateField(blank=True, null=True)),
                ("about", models.TextField(max_length=500)),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=apps.students.models.student_avatar_path,
                    ),
                ),
                (
                    "resume",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=apps.students.models.student_resume_path,
                    ),
                ),
                ("is_looking_for_job", models.BooleanField(default=True)),
                ("has_portfolio", models.BooleanField(default=False)),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="students",
                        to="about.city",
                    ),
                ),
                ("employment_types", models.ManyToManyField(to="about.employmenttype")),
                (
                    "grade",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="students",
                        to="about.grade",
                    ),
                ),
                (
                    "profession",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="students",
                        to="about.profession",
                    ),
                ),
            ],
            options={
                "verbose_name": "Студент",
                "verbose_name_plural": "Студенты",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="StudentSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.CharField(
                        choices=[
                            ("beginner", "новичок"),
                            ("basic", "базовый уровень"),
                            ("middle", "уверенный пользователь"),
                            ("professional", "профессионал"),
                        ],
                        default="beginner",
                        max_length=12,
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_skill",
                        to="about.skill",
                    ),
                ),
                (
                    "sudent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_skill",
                        to="students.student",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="skills",
            field=models.ManyToManyField(
                through="students.StudentSkill", to="about.skill"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="working_condition",
            field=models.ManyToManyField(to="about.workingcondition"),
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("organisation", models.CharField(max_length=250)),
                ("position", models.CharField(max_length=150)),
                ("started_at", models.DateTimeField()),
                ("finished_at", models.DateTimeField()),
                ("about", models.TextField(max_length=500)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="students.student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Работа",
                "verbose_name_plural": "Работа",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("institute", models.CharField(max_length=250)),
                ("speciality", models.CharField(max_length=250)),
                ("started_at", models.DateTimeField()),
                ("finished_at", models.DateTimeField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to="students.student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Образование",
                "verbose_name_plural": "Образование",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=25, unique=True)),
                (
                    "telegram",
                    models.CharField(
                        blank=True, max_length=150, null=True, unique=True
                    ),
                ),
                ("portfolio", models.URLField(blank=True, null=True)),
                (
                    "whatsapp",
                    models.CharField(blank=True, max_length=25, null=True, unique=True),
                ),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact",
                        to="students.student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ("-id",),
            },
        ),
    ]
