from rest_framework import serializers

from apps.students.models import Contact, Skill, Student
from apps.students.selectors import (calculate_skill_match,
                                     get_skill_match_status)
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
    skill_match = serializers.SerializerMethodField()

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
            "skill_match"
        )

    def get_skill_match(self, obj):
        student_skills = obj.skills.values_list("title", flat=True)
        filter_skills = self.context.get(
            "request").query_params.getlist("skills", [])
        skill_match_total = calculate_skill_match(
            student_skills, filter_skills)
        skill_match_status = get_skill_match_status(skill_match_total)
        return skill_match_status
