from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from apps.about.selectors import get_skills
from apps.students.models import Contact, Student


class DateSerializer(serializers.Serializer):
    """Сериализатор для отображения даты"""

    id = serializers.IntegerField(read_only=True)
    started_at = serializers.DateField(required=False)
    finished_at = serializers.DateField()


class EducationSerializer(DateSerializer):
    """Сериализатор для отображения образования студента"""

    institute = serializers.CharField(max_length=250)
    speciality = serializers.CharField(max_length=250)


class JobSerializer(DateSerializer):
    """Сериализатор для отображения опыта работы студента"""

    organisation = serializers.CharField(max_length=250)
    position = serializers.CharField(max_length=150)
    about = serializers.CharField(max_length=500)


class SkillSerializer(serializers.Serializer):
    """Сериализатор для отображения скиллов студента"""
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    score = serializers.IntegerField()


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения контактов студента"""

    class Meta:
        model = Contact
        fields = (
            "id",
            "email",
            "phone",
            "telegram",
            "portfolio",
            "whatsapp",
        )


class StudentCardSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения студента"""

    contact = ContactSerializer(read_only=True)
    city = serializers.StringRelatedField(read_only=True)
    profession = serializers.StringRelatedField(read_only=True)
    grade = serializers.StringRelatedField(read_only=True)
    employment_types = serializers.StringRelatedField(
        many=True, read_only=True
    )
    working_condition = serializers.StringRelatedField(
        many=True, read_only=True
    )
    educations = serializers.SerializerMethodField()
    jobs = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    experience = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = (
            "id",
            "name",
            "surname",
            "city",
            "profession",
            "grade",
            "employment_types",
            "working_condition",
            "contact",
            "avatar",
            "experience",
            "jobs",
            "educations",
            "about",
            "skills",
            "resume",
        )

    @extend_schema_field(field=EducationSerializer)
    def get_educations(self, obj):
        education = obj.educations.all()
        serializer = EducationSerializer(education, many=True)
        return serializer.data

    @extend_schema_field(field=JobSerializer)
    def get_jobs(self, obj):
        job = obj.jobs.all()
        serializer = JobSerializer(job, many=True)
        return serializer.data

    @extend_schema_field(field=SkillSerializer)
    def get_skills(self, obj):
        skills = get_skills(obj)
        serializer = SkillSerializer(skills, many=True)
        return serializer.data
