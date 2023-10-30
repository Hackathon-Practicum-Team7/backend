import pytest

from apps.about.models import (City, EmploymentType, Grade, Profession, Skill,
                               WorkingCondition)
from apps.api.v1.filters import StudentFilter
from apps.students.models import Student


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


@pytest.mark.django_db
def test_employment_types_filter():
    employment_type1 = EmploymentType.objects.create(title="Full-time")
    employment_type2 = EmploymentType.objects.create(title="Part-time")
    student1 = Student.objects.create()
    student1.employment_types.add(employment_type1)
    data = {"employment_types": [employment_type1.pk, employment_type2.pk]}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students


@pytest.mark.django_db
def test_working_condition_filter():
    condition1 = WorkingCondition.objects.create(title="Remote")
    condition2 = WorkingCondition.objects.create(title="Office")
    student1 = Student.objects.create()
    student1.working_condition.add(condition1)
    data = {"working_condition": [condition1.pk, condition2.pk]}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students


@pytest.mark.django_db
def test_has_portfolio_filter():
    student1 = Student.objects.create(has_portfolio=True)
    data = {"has_portfolio": True}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students


@pytest.mark.django_db
def test_grade_filter():
    grade = Grade.objects.create(title="Middle")
    student1 = Student.objects.create(grade=grade)
    data = {"grade": grade.pk}
    filter_set = StudentFilter(data, queryset=Student.objects.all())
    filtered_students = filter_set.qs
    assert student1 in filtered_students
