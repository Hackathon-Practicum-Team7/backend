import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from apps.about.models import (City, DirectionOfStudy, EmploymentType, Grade,
                               Profession, Skill, WorkingCondition)
from apps.students.models import Contact, Education, Job, Student, StudentSkill

User = get_user_model()


@pytest.fixture
def client_user():
    email = "mail@mail.ru"
    password = "password123"
    name = "Oleg"
    surname = "Lee"

    recruiter = User.objects.create_user(
        email=email,
        password=password,
        name=name,
        surname=surname
    )
    return recruiter


@pytest.fixture
def client_token(client_user):
    token = AccessToken.for_user(client_user)
    return {"access": str(token)}


@pytest.fixture
def client_client(client_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {client_token["access"]}')
    return client


@pytest.fixture
def city(db):
    return City.objects.create(title="Test City")


@pytest.fixture
def employment_type(db):
    return EmploymentType.objects.create(title="Test Employment Type")


@pytest.fixture
def grade(db):
    return Grade.objects.create(title="Test Grade")


@pytest.fixture
def profession(db):
    direction = DirectionOfStudy.objects.create(title="Designer")
    return Profession.objects.create(title="Test Profession", direction=direction)


@pytest.fixture
def skill(db):
    return Skill.objects.create(title="Test Skill")


@pytest.fixture
def working_condition(db):
    return WorkingCondition.objects.create(title="Test Working Condition")


@pytest.fixture
def student(db, city, employment_type, grade, profession, skill, working_condition):
    student = Student.objects.create(
        name="Oleg",
        surname="Lee",
        profession=profession,
        grade=grade,
        city=city,
        started_working=timezone.now(),
        about="Test Student",
        is_looking_for_job=True,
        has_portfolio=False
    )
    student.employment_types.set([employment_type])
    student.working_condition.set([working_condition])
    student.skills.set([skill])
    return student


@pytest.fixture
def student_with_resume():
    resume_file = SimpleUploadedFile("resume.pdf", b"file_content")
    student = Student.objects.create(name="Oleg", resume=resume_file)
    return student


@pytest.fixture
def contact(db, student):
    return Contact.objects.create(
        student=student,
        email="mail@mail.ru",
        phone="+7(926)000-00-00",
        telegram="http://t.me/ya",
        portfolio="http://ya.ru",
        whatsapp="+7(926)000-00-00"
    )


@pytest.fixture
def job(db, student):
    return Job.objects.create(
        student=student,
        organisation="Test Company",
        position="Test Position",
        started_at=timezone.now(),
        finished_at=timezone.now(),
        about="Test Job"
    )


@pytest.fixture
def education(db, student):
    return Education.objects.create(
        student=student,
        institute="Test Institute",
        speciality="Test Speciality",
        started_at=timezone.now(),
        finished_at=timezone.now()
    )


@pytest.fixture
def student_skill(db, student, skill):
    return StudentSkill.objects.create(
        student=student,
        skill=skill,
        score=StudentSkill.Score.BEGINNER
    )


@pytest.fixture
def skills(db):
    skills = []
    for title in ["Skill 1", "Skill 2", "Skill 3"]:
        skill = Skill.objects.create(title=title)
        skills.append(skill)
    return skills


@pytest.fixture
def current_year():
    return timezone.now().year
