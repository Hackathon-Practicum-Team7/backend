from django.contrib import admin

from apps.about.models import City, Profession, DirectionOfStudy


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "direction")
    empty_value_display = "-пусто-"


@admin.register(DirectionOfStudy)
class DirectionOfStudyAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
