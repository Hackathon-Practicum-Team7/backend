from rest_framework import serializers

from apps.students.models import Contact, Skill, Student
from .card import ContactSerializer, StudentCardSerializer


class ContactListSerializer(ContactSerializer):
    """Сериализатор для отображения контактов студента."""
    class Meta:
        model = Contact
        fields = ("email", "telegram")


class SkillListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения навыков студента."""
    class Meta:
        model = Skill
        fields = ("title",)


class StudentListSerializer(StudentCardSerializer):
    """Сериализатор для отображения списка студентов."""
    contact = ContactListSerializer(read_only=True)
    skills = SkillListSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = (
            "id",
            "avatar",
            "profession",
            "name",
            "surname",
            "grade",
            "city",
            "skills",
            "contact",
            "employment_types",
            "working_condition",
            "has_portfolio",
        )
