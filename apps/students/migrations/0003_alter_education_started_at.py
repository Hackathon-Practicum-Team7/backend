# Generated by Django 4.1 on 2023-10-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_alter_contact_telegram"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="started_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]