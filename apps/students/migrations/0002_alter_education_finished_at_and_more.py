# Generated by Django 4.1 on 2023-10-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="finished_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="education",
            name="started_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="finished_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="started_at",
            field=models.DateField(),
        ),
    ]