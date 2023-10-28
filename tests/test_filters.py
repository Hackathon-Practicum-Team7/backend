import pytest
from apps.students.models import Student
from apps.api.v1.filters import StudentFilter
from apps.about.models import Profession, Skill, City


@pytest.mark.django_db
def test_profession_filter():
    profession = Profession.objects.create(title="Engineer")
    student1 = Student.objects.create(profession=profession)
    data = {"profession": profession.pk}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students


@pytest.mark.django_db
def test_skills_filter():
    skill1 = Skill.objects.create(title="Python")
    skill2 = Skill.objects.create(title="JavaScript")
    student1 = Student.objects.create()
    student1.skills.add(skill1, skill2)
    data = {"skills": [skill1.pk, skill2.pk]}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students


@pytest.mark.django_db
def test_city_filter():
    city = City.objects.create(title="Moscow")
    student1 = Student.objects.create(city=city) 
    data = {"city__title": "Moscow"}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students
