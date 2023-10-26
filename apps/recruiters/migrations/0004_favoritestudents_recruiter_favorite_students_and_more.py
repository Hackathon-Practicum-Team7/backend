# Generated by Django 4.1 on 2023-10-26 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_education_started_at'),
        ('recruiters', '0003_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
        migrations.AddField(
            model_name='recruiter',
            name='favorite_students',
            field=models.ManyToManyField(through='recruiters.FavoriteStudents', to='students.student'),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.AddField(
            model_name='favoritestudents',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoritestudents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='students.student'),
        ),
    ]
