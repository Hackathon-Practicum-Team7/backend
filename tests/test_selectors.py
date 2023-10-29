import uuid

import pytest
from rest_framework import exceptions

from apps.about.selectors import get_cities, get_direction_of_study, get_skills
from apps.students.models import Student
from apps.students.selectors import (calculate_skill_match, get_all_students,
                                     get_selected_students,
                                     get_skill_match_status, get_student)


def create_test_students():
    student1 = Student.objects.create(name="Student1", is_looking_for_job=True)
    student2 = Student.objects.create(name="Student2", is_looking_for_job=True)
    student3 = Student.objects.create(name="Student3", is_looking_for_job=True)
    return student1, student2, student3


@pytest.mark.django_db
def test_get_all_students(student):
    queryset = get_all_students()
    assert student in queryset


@pytest.mark.django_db
def test_get_all_students_with_skills():
    student1, student2, student3 = create_test_students()
    skills = ["Python", "JavaScript"]
    queryset = get_all_students(skills)
    expected_students = {student1, student2, student3}
    assert set(queryset) == expected_students


@pytest.mark.django_db
def test_get_student():
    student1, _, _ = create_test_students()
    student = get_student(student1.id)
    assert student == student1


@pytest.mark.django_db
def test_get_student_not_found():
    with pytest.raises(exceptions.NotFound):
        get_student(uuid.uuid4())


@pytest.mark.django_db
def test_get_selected_students():
    student1, student2, student3 = create_test_students()
    students_id = [{"id": str(student1.id)}, {"id": str(student2.id)}]
    queryset = get_selected_students(students_id)
    assert student1 in queryset
    assert student2 in queryset
    assert student3 not in queryset


@pytest.mark.django_db
def test_get_selected_students_empty_ids():
    _, _, _ = create_test_students()
    students_id = []
    queryset = get_selected_students(students_id)
    assert not queryset.exists()


@pytest.mark.django_db
def test_get_selected_students_invalid_ids():
    student1, _, _ = create_test_students()
    students_id = [{"id": str(student1.id)}, {"id": str(uuid.uuid4())}]
    queryset = get_selected_students(students_id)
    assert student1 in queryset
    assert not queryset.filter(id=uuid.uuid4()).exists()


@pytest.mark.django_db
def test_get_skill_match_status():
    assert get_skill_match_status(80) == 100
    assert get_skill_match_status(60) == 75
    assert get_skill_match_status(40) == 50
    assert get_skill_match_status(10) == 25
    assert get_skill_match_status(0) == 0


@pytest.mark.django_db
def test_calculate_skill_match():
    student_skills = ["Python", "JavaScript"]
    filter_skills = ["Python", "JavaScript", "CSS"]
    match = calculate_skill_match(student_skills, filter_skills)
    expected_status = get_skill_match_status(match)
    assert expected_status == 75


@pytest.mark.django_db
def test_get_cities(city):
    cities = get_cities()
    assert len(cities) == 1
    assert cities[0].title == "Test City"


@pytest.mark.django_db
def test_get_direction_of_study(profession):
    directions = get_direction_of_study()
    assert len(directions) == 1
    assert directions[0].title == "Designer"


@pytest.mark.django_db
def test_get_skills(skill, student):
    student.skills.add(skill)
    skills = get_skills(student)
    assert len(skills) == 1
    assert skills[0].title == "Test Skill"
