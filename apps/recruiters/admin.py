from django.contrib import admin

from .models import Recruiter


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "surname")
    empty_value_display = "-пусто-"

    def save_model(self, request, obj, form, change):
        password = form.data.get('password')
        obj.set_password(password)
        obj.save()
