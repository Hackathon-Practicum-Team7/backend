# Generated by Django 4.1 on 2023-10-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="finished_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]
